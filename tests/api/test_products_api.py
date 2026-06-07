import os
from utils.api_client import APIClient


def test_get_all_products():
    client = APIClient("https://fakestoreapi.com")

    response = client.get("/products")

    if response.status_code == 403:
        assert os.getenv("CI") != "true", "API blocked in CI environment"

    assert response.status_code in [200, 201]

    if response.status_code == 200:
        assert isinstance(response.json(), list)