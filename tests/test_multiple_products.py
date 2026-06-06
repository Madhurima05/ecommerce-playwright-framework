from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_multiple_products(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack()
    inventory.add_bike_light()

    assert inventory.get_cart_count() == 2