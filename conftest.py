import pytest
import os
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:

        # Detect CI environment (GitHub Actions)
        is_ci = os.getenv("CI") == "true"

        browser = p.chromium.launch(
            headless=is_ci
        )

        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()