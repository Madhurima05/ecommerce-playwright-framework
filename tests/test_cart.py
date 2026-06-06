from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_product_to_cart()
    inventory.open_cart()

    assert "cart" in page.url