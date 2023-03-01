import requests
import logging

logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, base_url, auth=None):
        self.base_url = base_url
        self.auth = auth

    def get(self, path=None):
        url = self.base_url + path
        headers = self._get_headers()
        response = requests.get(url, headers=headers, auth=self.auth)
        response.raise_for_status()
        return response.json(), response.status_code, response.headers

    def post(self, data, path=None):
        url = self.base_url + path
        headers = self._get_headers()
        response = requests.post(url, json=data, headers=headers, auth=self.auth)
        response.raise_for_status()
        return response.json(), response.status_code, response.headers

    def put(self, data, path=None):
        url = self.base_url + path
        headers = self._get_headers()
        response = requests.put(url, json=data, headers=headers, auth=self.auth)
        response.raise_for_status()
        return response.json(), response.status_code, response.headers

    def patch(self, data, path=None):
        url = self.base_url + path
        headers = self._get_headers()
        response = requests.patch(url, json=data, headers=headers, auth=self.auth)
        response.raise_for_status()
        return response.json(), response.status_code, response.headers

    def delete(self, path=None):
        url = self.base_url + path
        headers = self._get_headers()
        response = requests.delete(url, headers=headers, auth=self.auth)
        response.raise_for_status()
        return response.json(), response.status_code, response.headers

    def _get_headers(self):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if self.auth:
            headers["Authorization"] = "Bearer " + self.auth.token
        return headers
