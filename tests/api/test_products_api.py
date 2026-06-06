from utils.api_client import APIClient


def test_get_all_products():
    client = APIClient("https://fakestoreapi.com")

    response = client.get("/products")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0