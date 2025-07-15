from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.cart_page import CartPage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ADD_CART = (By.XPATH, "//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']")
        self.PRODUCT_TITLE = (By.XPATH, "//span[@id='productTitle']")
        self.CART = (By.XPATH,"//div[@id='nav-cart-count-container']")

    def get_product_name(self):
        return self.get_text(self.PRODUCT_TITLE)

    def add_to_cart(self):
        product_name = self.get_product_name()
        self.click(self.ADD_CART)
        self.click(self.CART)
        cart = CartPage(self.driver)
        cart.set_expected_product_name(product_name)
        return cart
