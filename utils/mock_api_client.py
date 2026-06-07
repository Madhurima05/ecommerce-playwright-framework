import json
import os


class MockAPIClient:

    def __init__(self):
        base_path = os.path.join(os.path.dirname(__file__), "..", "tests", "api", "mock_data")
        self.products_file = os.path.join(base_path, "products.json")

    def get_all_products(self):
        with open(self.products_file, "r") as file:
            return json.load(file)

    def get_product_by_id(self, product_id):
        products = self.get_all_products()

        for product in products:
            if product["id"] == product_id:
                return product

        return None