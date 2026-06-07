from utils.api_client import APIClient


def test_get_all_products():
    client = APIClient("https://fakestoreapi.com")

    response = client.get("/products")

    assert response.status_code in [200, 201], f"API failed with {response.status_code}"

    data = response.json()
    assert isinstance(data, list)