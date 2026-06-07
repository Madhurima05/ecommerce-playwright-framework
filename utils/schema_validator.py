class SchemaValidator:

    @staticmethod
    def validate_status_code(response, expected_codes=(200, 201)):
        assert response.status_code in expected_codes, (
            f"Unexpected status code: {response.status_code}"
        )

    @staticmethod
    def validate_product_schema(product):
        required_keys = ["id", "title", "price", "category"]

        for key in required_keys:
            assert key in product, f"Missing key: {key}"

        assert isinstance(product["id"], int)
        assert isinstance(product["title"], str)
        assert isinstance(product["price"], (int, float))
        assert isinstance(product["category"], str)