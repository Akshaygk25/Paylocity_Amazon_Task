import time
import pytest
from pages.product_page import ProductPage
from pages.results_page import ResultsPage
from pages.home_page import HomePage

# Parametrize the test
@pytest.mark.parametrize("search_term,brands,min_price,max_price", [
    ("smartwatches", ["Noise", "boAt", "Fire-Boltt", "Fastrack"], 1000, 2000)])
#Note - We'll be using price range of 1000 to 2000 only
def test_amazon_search(browser_instance, search_term, brands, min_price, max_price):
    driver = browser_instance
    home_page = HomePage(driver)
    home_page.open_amazon()
    assert home_page.wait_for_home_title()
    home_page.search_amazon(search_term)

    results = ResultsPage(driver)
    assert results.wait_for_results_title(search_term)

    for brand in brands:
        results.filter_by_brand(brand)
        results.set_price_slider_range(min_price, max_price)

        prices = results.get_prices()
        for price in prices:
            assert min_price < price < max_price, f"Price {price} is out of range"

        results.sort_by()
        results.highest_prod()

        product = ProductPage(driver)
        cart = product.add_to_cart()
        cart.verify_product_in_cart()

        cart.close_current_window()
        cart.switch_to_parent_window()
        results.clear_brand()
        time.sleep(5)
        results.filter_by_brand(brand)

        driver.back()
        driver.refresh()
        time.sleep(8)
