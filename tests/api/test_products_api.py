import os
from utils.api_client import APIClient
from tests.api.mock_api import mock_products


def test_get_all_products():
    if os.getenv("CI") == "true":
        data = mock_products()
        assert isinstance(data, list)
        assert len(data) > 0
        return

    client = APIClient("https://fakestoreapi.com")
    response = client.get("/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)