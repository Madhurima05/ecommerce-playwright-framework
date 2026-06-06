from pages.login_page import LoginPage


def test_locked_user(page):
    login = LoginPage(page)

    login.open()
    login.login("locked_out_user", "secret_sauce")

    assert login.is_error_displayed()