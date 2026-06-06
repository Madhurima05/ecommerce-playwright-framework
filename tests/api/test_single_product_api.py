from utils.api_client import APIClient


def test_get_single_product():
    client = APIClient("https://fakestoreapi.com")

    response = client.get("/products/1")

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert data["id"] == 1