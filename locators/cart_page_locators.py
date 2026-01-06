from selenium.webdriver.common.by import By

class CartPageLocators:

    ORDER_OVERVIEW = (By.CSS_SELECTOR, '.col')
    CART_ICON_COUNT = (By.XPATH, '//sup[contains(@class,"my_cart_quantity")]')
    #header_title_loc = (By.TAG_NAME, 'h1')
