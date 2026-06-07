import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
            "Connection": "keep-alive"
        }

    def get(self, endpoint):
        url = self.base_url + endpoint

        response = requests.get(url, headers=self.headers, timeout=10)

        return response