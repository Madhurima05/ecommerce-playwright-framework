from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def test_order_confirmation(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_product_to_cart()
    inventory.open_cart()

    checkout.start_checkout()

    checkout.fill_details(
        "John",
        "Doe",
        "12345"
    )

    checkout.complete_checkout()

    assert (
        checkout.get_success_message()
        == "Thank you for your order!"
    )