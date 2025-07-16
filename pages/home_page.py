from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")

    def open_amazon(self):
        self.driver.get("https://www.amazon.in/")
        return self

    def wait_for_home_title(self, expected_title_part="Amazon"):
        WebDriverWait(self.driver, 15).until(EC.title_contains(expected_title_part))
        return expected_title_part.lower() in self.driver.title.lower()


    def search_amazon(self, product_name):
        self.send_keys(self.search_box, product_name)
        self.click(self.search_button)
