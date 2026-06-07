import os
import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.is_ci = os.getenv("CI") == "true"

    def get(self, endpoint):
        url = self.base_url + endpoint

        # CI SAFE MODE (mock response instead of real API call)
        if self.is_ci:
            return MockResponse(endpoint)

        return requests.get(url)


class MockResponse:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.status_code = 200

    def json(self):
        if self.endpoint == "/products":
            return [
                {"id": 1, "title": "mock product", "price": 10},
                {"id": 2, "title": "mock product 2", "price": 20},
            ]

        if self.endpoint.startswith("/products/"):
            return {"id": 1, "title": "mock product", "price": 10}

        return {}