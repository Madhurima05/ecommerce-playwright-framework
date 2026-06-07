from utils.api_client import APIClient


def test_get_single_product():
    client = APIClient("https://fakestoreapi.com")

    response = client.get("/products/1")

    assert response.status_code in [200, 201], f"API failed with {response.status_code}"

    data = response.json()
    assert "id" in data