from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGO = (By.CSS_SELECTOR, "img[alt*='Logo']")
    SIGN_IN_LINK = (By.LINK_TEXT, "Sign in")
    CONTACT_LINK = (By.LINK_TEXT, "Contact Us")
    CART_LINK = (By.CSS_SELECTOR, "a.shopping-cart")

    # Search elements
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='s']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # Product elements
    PRODUCT_CARDS = (By.CSS_SELECTOR, "article.product-miniature")

    # Categories
    DESKS_CATEGORY = (By.LINK_TEXT, "Desks")
    FURNITURES_CATEGORY = (By.LINK_TEXT, "Furnitures")
