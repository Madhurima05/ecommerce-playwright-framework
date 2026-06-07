from utils.api_client import APIClient
from utils.schema_validator import SchemaValidator


def test_get_all_products():
    client = APIClient("https://fakestoreapi.com")

    response = client.get("/products")

    SchemaValidator.validate_status_code(response)

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    SchemaValidator.validate_keys(data[0], ["id", "title", "price"])


def test_get_single_product():
    client = APIClient("https://fakestoreapi.com")

    response = client.get("/products/1")

    SchemaValidator.validate_status_code(response)

    data = response.json()

    SchemaValidator.validate_keys(data, ["id", "title", "price"])