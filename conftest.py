import pytest
from playwright.sync_api import sync_playwright
import os


@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:

        is_ci = os.getenv("CI") == "true"

        browser = p.chromium.launch(headless=is_ci)
        context = browser.new_context()

        yield context

        browser.close()


@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page