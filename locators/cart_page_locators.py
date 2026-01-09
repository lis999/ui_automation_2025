from selenium.webdriver.common.by import By

class CartPageLocators:

    ORDER_OVERVIEW = (By.CSS_SELECTOR, '.col')
    CART_ICON_COUNT = (By.XPATH, '(//sup[contains(@class,"my_cart_quantity")])[1]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'i[class="oi oi-search fa-stack lh-lg"]' )
    SEARCH_FIELD = (By.CSS_SELECTOR, 'div[style="display: block;"]')
    PHONE_NUMBER_FIELD = (By.XPATH, '(//span[@class="o_force_ltr"])[1]')
