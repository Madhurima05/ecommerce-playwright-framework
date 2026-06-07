import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

        self.default_headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        }

    def get(self, endpoint, headers=None, params=None):
        url = self.base_url + endpoint

        merged_headers = self.default_headers.copy()
        if headers:
            merged_headers.update(headers)

        response = requests.get(url, headers=merged_headers, params=params)

        return response

    def post(self, endpoint, data=None, headers=None):
        url = self.base_url + endpoint

        merged_headers = self.default_headers.copy()
        if headers:
            merged_headers.update(headers)

        response = requests.post(url, json=data, headers=merged_headers)

        return response