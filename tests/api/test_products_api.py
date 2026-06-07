from utils.api_client import APIClient


def test_get_all_products():
    client = APIClient("https://fakestoreapi.com")

    response = client.get("/products")

    assert response.status_code in [200, 201]
    assert isinstance(response.json(), list)