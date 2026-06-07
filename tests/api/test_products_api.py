from utils.mock_api_client import MockAPIClient
from utils.schema_validator import SchemaValidator


def test_get_all_products():
    client = MockAPIClient()

    response = client.get_all_products()

    assert isinstance(response, list)
    assert len(response) > 0

    SchemaValidator.validate_product_schema(response[0])


def test_get_single_product():
    client = MockAPIClient()

    response = client.get_product_by_id(1)

    assert response is not None
    assert response["id"] == 1

    SchemaValidator.validate_product_schema(response)