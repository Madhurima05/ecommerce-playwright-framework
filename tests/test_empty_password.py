from pages.login_page import LoginPage


def test_empty_password(page):
    login = LoginPage(page)

    login.open()
    login.login("standard_user", "")

    assert login.is_error_displayed()