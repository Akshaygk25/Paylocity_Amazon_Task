from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.PRODUCTS = (
        By.XPATH, "//div[@class='sc-list-item-content']//span[@class='a-truncate-cut' and @aria-hidden='true']")
        self.expected_product = None

    def cart_items(self):
        return self.get_text_of_elements(self.PRODUCTS)

    def set_expected_product_name(self, product_name):
        self.expected_product = product_name

    def get_cart_product_name(self):
        return self.get_text(self.PRODUCTS)

    def verify_product_in_cart(self):
        actual_product = self.get_cart_product_name().strip()
        expected_keywords = self.expected_product.lower().split()
        match_found = any(keyword in actual_product.lower() for keyword in expected_keywords)
        assert match_found, f"No expected keyword found in cart product name. Expected any of '{self.expected_product}' in '{actual_product}'"



