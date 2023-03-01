import requests
from response import Response

class Request:
    def __init__(self, method, url, headers=None, params=None, data=None, json=None):
        self.method = method
        self.url = url
        self.headers = headers or {}
        self.params = params or {}
        self.data = data
        self.json = json

    def send(self):
        response = requests.request(
            method=self.method,
            url=self.url,
            headers=self.headers,
            params=self.params,
            data=self.data,
            json=self.json,
        )
        return Response(response)
