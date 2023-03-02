import jwt
import aiohttp
from aiohttp import ClientSession, ClientResponseError
from requests.auth import HTTPDigestAuth
from requests_oauthlib import OAuth1
from . import response_client


class AuthMethod:
    BASIC = "Basic_Authentication"
    DIGEST = "Digest_Authentication"
    OAUTH = "OAuth_Authentication"
    JWT = "jwt"


class Request:
    def __init__(self, method, url, headers=None, params=None, data=None, json=None, auth=None):
        self.method = method
        self.url = url
        self.headers = headers or {}
        self.params = params or {}
        self.data = data
        self.json = json
        self.auth = auth

    async def send(self):
        async with ClientSession() as session:
            if self.auth:
                if self.auth.method_for_auth == AuthMethod.BASIC:
                    session.auth = aiohttp.BasicAuth(
                        self.auth.username, self.auth.password
                    )
                elif self.auth.method_for_auth == AuthMethod.DIGEST:
                    session.auth = aiohttp.DigestAuth(
                        self.auth.username, self.auth.password
                    )
                elif self.auth.method_for_auth == AuthMethod.OAUTH:
                    session.auth = aiohttp.OAuth1Auth(
                        self.auth.client_key,
                        self.auth.client_secret,
                        self.auth.resource_owner_key,
                        self.auth.resource_owner_secret,
                    )
                elif self.auth.method_for_auth == AuthMethod.JWT:
                    token = jwt.encode(
                        {"user": "my_username"}, self.auth.secret_key, algorithm="HS256"
                    )
                    self.headers = {"Authorization": f"Bearer {token.decode()}"}

            async with session.request(
                method=self.method,
                url=self.url,
                headers=self.headers,
                params=self.params,
                json=self.json,
                auth=session.auth,
            ) as response:
                if response.status >= 400:
                    raise ClientResponseError(
                        response.request_info,
                        response.history,
                        status=response.status,
                        message=response.reason,
                        headers=response.headers,
                    )

                response_client.Response(response)
                return response
