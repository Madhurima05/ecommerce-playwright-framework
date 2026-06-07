import os
from utils.api_client import APIClient


def test_get_single_product():
    client = APIClient("https://fakestoreapi.com")

    response = client.get("/products/1")

    if response.status_code == 403:
        assert os.getenv("CI") != "true", "API blocked in CI environment"

    assert response.status_code in [200, 201]

    if response.status_code == 200:
        data = response.json()
        assert "id" in data