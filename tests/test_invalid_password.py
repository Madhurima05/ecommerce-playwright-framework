from pages.login_page import LoginPage


def test_invalid_password(page):
    login = LoginPage(page)

    login.open()
    login.login("standard_user", "wrong_password")

    assert login.is_error_displayed()