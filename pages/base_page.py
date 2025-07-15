import platform
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,15)
        self.actions = ActionChains(self.driver)


    def visibility_of_element_located(self,locator):
        return self.wait.until(visibility_of_element_located(locator))

    def visibility_of_elements_located(self,locator):
        return self.wait.until(self.visibility_of_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        self.visibility_of_element_located(locator).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_text_of_elements(self, locator):
        elements = self.wait.until(self.visibility_of_elements_located(locator))
        items = []
        for ele in elements:
            items.append(ele.text)
        return items


    def open_in_new_tab(self, locator):
        modifier_key = Keys.COMMAND if platform.system() == "Darwin" else Keys.CONTROL
        element = self.wait.until(EC.element_to_be_clickable(locator))

        # Open link in new tab
        self.actions.key_down(modifier_key).click(element).key_up(modifier_key).perform()

        # Short hard wait to give the tab a chance to open
        time.sleep(2)

    def switch_to_parent_window(self):
        parent_handle = self.driver.window_handles[0]
        self.driver.switch_to.window(parent_handle)

    def close_current_window(self):
        self.driver.close()

    def switch_to_window(self, index):
        handles = self.driver.window_handles
        if index < len(handles):
            self.driver.switch_to.window(handles[index])
        else:
            raise IndexError(f"No window at index {index}. Total open windows: {len(handles)}")

    def is_visible(self,locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_title_contains(self, text, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.title_contains(text))
        return text.lower() in self.driver.title.lower()






