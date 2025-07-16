# Test Use Cases: Amazon.in Search, Filter, and Add-to-Cart Automation

## Objective

This document outlines the test scenarios automated to validate the core e-commerce functionalities on [Amazon.in](https://www.amazon.in), specifically focusing on:

- Search functionality
- Product filtering by brand and price
- Sorting
- Add-to-cart workflow

---

## 1. Search Functionality

### Use Cases:
- Verify that the search bar is present and functional.
- Validate entering a product keyword (e.g., "smartwatches") displays relevant results.
- Check if the page title contains the searched keyword.
- Ensure the first set of results are loaded properly.

---

## 2. Filter Functionality

### Use Cases:

#### Brand Filter:
- Validate that brand filters (e.g., Noise, boAt, Fire-Boltt) are available on the sidebar.
- Test selecting a brand applies the correct filter and refreshes results.
- Verify product titles or branding elements reflect the selected brand.

#### Price Range Filter:
- Check the presence and functionality of the price range slider.
- Set a minimum and maximum price (e.g., ₹1000–₹2000).
- Verify the product listings fall within the selected price range.
- Ensure the "Go" button applies the price filter.

#### Clearing Filters:
- Validate that clearing filters resets the result set.
- Ensure previously applied filters are removed from the UI.

---

## 3. Sorting Functionality

### Use Cases:
- Verify the presence of sorting dropdown.
- Test the “Price: High to Low” sorting option.
- Ensure results re-order accordingly and the most expensive item appears first.

---

## 4. Add to Cart

### Use Cases:
- Click on the highest-priced product and open it in a new tab.
- Validate that product details load correctly (product title, price, etc.).
- Click on the "Add to Cart" button.
- Verify redirection or update of cart count after adding.
- Navigate to cart and confirm that the correct product is listed.

---

## 5. Miscellaneous

### Use Cases:
- Ensure browser tab/window management is handled properly after switching.
- Handle dynamic waits for elements such as filters, product results, and price sliders.
- Validate that the test is data-driven using external test data (Eg - search terms, brands, price range)
- Capture screenshots and logs for failures in test reports (Eg - Allure integration).
