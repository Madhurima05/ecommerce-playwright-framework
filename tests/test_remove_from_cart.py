from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_remove_product_from_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack()

    assert inventory.get_cart_count() == 1

    inventory.remove_backpack()

    assert inventory.get_cart_count() == 0