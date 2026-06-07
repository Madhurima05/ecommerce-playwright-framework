class SchemaValidator:

    @staticmethod
    def validate_keys(response_json, expected_keys):
        if isinstance(response_json, list):
            response_json = response_json[0]

        missing_keys = [key for key in expected_keys if key not in response_json]

        assert not missing_keys, f"Missing keys: {missing_keys}"

        return True

    @staticmethod
    def validate_status_code(response, expected_codes=(200, 201)):
        assert response.status_code in expected_codes, (
            f"Unexpected status code: {response.status_code}"
        )