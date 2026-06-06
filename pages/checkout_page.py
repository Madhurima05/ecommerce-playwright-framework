class CheckoutPage:
    def __init__(self, page):
        self.page = page

        self.checkout_btn = "#checkout"

        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"

        self.continue_btn = "#continue"
        self.cancel_btn = "#cancel"
        self.finish_btn = "#finish"

        self.error_message = "[data-test='error']"
        self.complete_header = ".complete-header"

    def start_checkout(self):
        self.page.click(self.checkout_btn)

    def fill_details(self, first_name, last_name, postal_code):
        self.page.fill(self.first_name, first_name)
        self.page.fill(self.last_name, last_name)
        self.page.fill(self.postal_code, postal_code)

    def continue_checkout(self):
        self.page.click(self.continue_btn)

    def finish_checkout(self):
        self.page.click(self.finish_btn)

    def complete_checkout(self):
        self.continue_checkout()
        self.finish_checkout()

    def cancel_checkout(self):
        self.page.click(self.cancel_btn)

    def is_error_displayed(self):
        return self.page.locator(self.error_message).is_visible()

    def get_error_message(self):
        return self.page.locator(self.error_message).text_content()

    def get_success_message(self):
        return self.page.locator(self.complete_header).text_content()