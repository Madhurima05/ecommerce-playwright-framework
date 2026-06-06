from pages.login_page import LoginPage


def test_empty_username(page):
    login = LoginPage(page)

    login.open()
    login.login("", "secret_sauce")

    assert login.is_error_displayed()