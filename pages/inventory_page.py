class InventoryPage:
    def __init__(self, page):
        self.page = page

        self.backpack_add_btn = (
            "button[data-test='add-to-cart-sauce-labs-backpack']"
        )

        self.bike_light_add_btn = (
            "button[data-test='add-to-cart-sauce-labs-bike-light']"
        )

        self.backpack_remove_btn = (
            "button[data-test='remove-sauce-labs-backpack']"
        )

        self.cart_icon = ".shopping_cart_link"
        self.cart_badge = ".shopping_cart_badge"

    # Existing method used by old tests
    def add_product_to_cart(self):
        self.page.click(self.backpack_add_btn)

    # New methods
    def add_backpack(self):
        self.page.click(self.backpack_add_btn)

    def add_bike_light(self):
        self.page.click(self.bike_light_add_btn)

    def remove_backpack(self):
        self.page.click(self.backpack_remove_btn)

    def open_cart(self):
        self.page.click(self.cart_icon)

    def get_cart_count(self):
        badge = self.page.locator(self.cart_badge)

        if badge.count() == 0:
            return 0

        return int(badge.text_content())