import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = self.base_url + endpoint

        response = requests.get(url, timeout=10)

        return response