from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGO = (By.CSS_SELECTOR, "img[alt='My Website']")
    SIGN_IN_LINK = (By.CSS_SELECTOR, "a[href='/web/login']")
    CONTACT_LINK = (By.CSS_SELECTOR, "a[href='/contactus']")
    CART_LINK = (By.CSS_SELECTOR, "i.fa.fa-shopping-cart.fa-stack")

    # Search elements
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit'], i.oi.oi-search")

    # Product elements
    PRODUCT_CARDS = (By.CSS_SELECTOR, "div.o_wsale_product_grid_wrapper")

    # Categories
    DESKS_CATEGORY = (By.LINK_TEXT, "Desks")
    FURNITURES_CATEGORY = (By.LINK_TEXT, "Furnitures")
