from selenium.webdriver.common.by import By


class ProductOfficeLocators:
    PRODUCT_CATEGORY_NAME = (By.CSS_SELECTOR, 'div.row.align-items-center')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add_to_cart')
    OFFICE_SOFTWARE_PRICE = (By.XPATH, '(//*[@class="oe_currency_value"])[1]')
    NUMBER_ITEMS_CART = (By.XPATH, '(//sup[contains(@class, "my_cart_quantity")])[1]')

