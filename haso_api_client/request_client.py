import requests
import jwt
from requests.auth import HTTPDigestAuth
from requests_oauthlib import OAuth1
from . import response_client


class Request:
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    def __init__(self, method, url, headers=None, params=None, data=None, json=None, auth=None):
        self.method = method
        self.url = url
        self.headers = headers or {}
        self.params = params or {}
        self.data = data
        self.json = json
        self.auth = auth

    async def send(self):
        try:
            if self.auth:
                method_for_auth = self.auth.method_for_auth
                if method_for_auth == "Basic_Authentication":
                    self.auth = (self.auth.username, self.auth.password)
                elif method_for_auth == "Digest_Authentication":
                    self.auth = HTTPDigestAuth(self.auth.username, self.auth.password)
                elif method_for_auth == "OAuth_Authentication":
                    self.auth = OAuth1(
                        self.auth.client_key,
                        self.auth.client_secret,
                        self.auth.resource_owner_key,
                        self.auth.resource_owner_secret,
                    )

                elif method_for_auth == "jwt":
                    token = jwt.encode(
                        {"user": "my_username"}, self.auth.secret_key, algorithm="HS256"
                    )
                    self.headers = {"Authorization": f"Bearer {token.decode()}"}
                    self.session.auth = self.auth
                    self.session.headers.update(self.headers)
                    response = await self.session.request(
                        method=self.method,
                        url=self.url,
                        headers=self.headers,
                        params=self.params,
                        json=self.json,
                    )

            else:
                self.session.auth = self.auth
                self.session.headers.update(self.headers)
                response = await self.session.request(
                    method=self.method,
                    url=self.url,
                    auth=self.auth,
                    headers=self.headers,
                    params=self.params,
                    json=self.json,
                )

                response_client.Response(response)
                response.raise_for_status()
                return response

        except requests.exceptions.HTTPError as e:
            raise e
