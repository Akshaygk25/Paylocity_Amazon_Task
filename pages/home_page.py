from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")

    def open_amazon(self):
        self.driver.get("https://www.amazon.in/")
        return self

    def search_amazon(self, product_name):
        self.send_keys(self.search_box, product_name)
        self.click(self.search_button)
