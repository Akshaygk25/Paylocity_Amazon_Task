import re
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.go = (By.XPATH, "//div//input[@class='a-button-input']")
        self.go1 = (By.XPATH, "//input[@class='a-button-input']")
        self.price_elements = (By.XPATH, "//div[@class='puisg-row']//span[@class='a-price-whole']")
        self.SORT_BY = (By.XPATH,"//span[@data-action='a-dropdown-button']")
        self.SORT_BY_HIGH_TO_LOW = (By.XPATH, "//a[text()='Price: High to Low']")
        self.FIRST_PRODUCT = (By.XPATH, "//div[@data-component-type='s-search-result']")


    def wait_for_results_title(self, keyword):
        WebDriverWait(self.driver, 15).until(EC.title_contains(keyword))
        return keyword.lower() in self.driver.title.lower()

    def filter_by_brand(self,brand):
        self.click((By.XPATH, f"//li//span[text()='{brand}']"))

    def set_price_slider_range(self, min_price, max_price):
        wait = WebDriverWait(self.driver, 10)

        if min_price > max_price:
            raise ValueError('Min price should be more than Max price')

        min_slider = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='range' and @aria-label='Minimum price']")))
        max_slider = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='range' and @aria-label='Maximum price']")))

        def get_current_prices():
            min_text = self.driver.find_element(By.XPATH, "//label[contains(@class,'sf-lower-bound-label')]//span").text
            max_text = self.driver.find_element(By.XPATH, "//label[contains(@class,'sf-upper-bound-label')]//span").text
            min_val = int(re.sub(r"[^\d]", "", min_text))
            max_val = int(re.sub(r"[^\d]", "", max_text))
            return min_val, max_val

        # Adjust lower slider with arrow keys
        for _ in range(100):
            current_min, _ = get_current_prices()
            if current_min >= min_price:
                break
            min_slider.send_keys(Keys.ARROW_RIGHT)
            time.sleep(0.1)

        # Adjust upper slider with arrow keys
        for _ in range(100):
            _, current_max = get_current_prices()
            if current_max <= max_price:
                break
            max_slider.send_keys(Keys.ARROW_LEFT)
            time.sleep(0.1)

        final_min, final_max = get_current_prices()
        print(f"Final slider values: ₹{final_min} - ₹{final_max}")

        self.click(self.go1)

        assert final_min >= min_price, f"Lower price not set correctly: ₹{final_min} < ₹{min_price}"
        assert final_max <= max_price, f"Upper price not set correctly: ₹{final_max} > ₹{max_price}"

    def get_prices(self):
        # Find all product containers
        product_cards = self.wait.until(presence_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']")))

        prices = []

        for card in product_cards:
            try:
                whole = card.find_element(By.CLASS_NAME, "a-price-whole").text.strip()
                fraction = card.find_element(By.CLASS_NAME, "a-price-fraction").text.strip()
                if whole:
                    price_str = whole.replace(",", "") + "." + fraction
                    prices.append(float(price_str))
            except Exception:
                # Skip cards without proper price
                continue

        return prices


    def sort_by(self):
        self.click(self.SORT_BY)
        self.click(self.SORT_BY_HIGH_TO_LOW)

    def highest_prod(self):
        current_handles = self.driver.window_handles
        product_card = self.wait.until(EC.presence_of_element_located(self.FIRST_PRODUCT))

        # Locate <a> inside the first product
        link_element = product_card.find_element(By.TAG_NAME, "a")
        href = link_element.get_attribute("href")

        if not href:
            raise Exception("First product does not contain a clickable link")

        # Open the link in a new tab
        self.driver.execute_script(f"window.open('{href}', '_blank');")

        # Wait until new tab is opened
        self.wait.until(
            lambda d: len(d.window_handles) > len(current_handles),
            message="New tab did not open in time"
        )

        new_tab = [h for h in self.driver.window_handles if h not in current_handles][0]
        self.driver.switch_to.window(new_tab)

    def clear_brand(self):
        locator = (By.XPATH, "//div//span[text()='Clear']")
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)


