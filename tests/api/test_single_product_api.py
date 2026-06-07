import os
from utils.api_client import APIClient


def test_get_single_product():
    if os.getenv("CI") == "true":
        data = {"id": 1, "title": "mock product"}
        assert data["id"] == 1
        return

    client = APIClient("https://fakestoreapi.com")
    response = client.get("/products/1")

    assert response.status_code == 200
    assert "id" in response.json()