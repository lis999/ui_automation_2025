from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGO = (By.CSS_SELECTOR, "img[alt='My Website']")
    SIGN_IN_LINK = (By.CSS_SELECTOR, "a[href='/web/login']")
    CONTACT_LINK = (By.CSS_SELECTOR, "a[href='/contactus']")
    CART_LINK = (By.CSS_SELECTOR, "i.fa.fa-shopping-cart.fa-stack")

    # Search elements
    SEARCH_INPUT = (By.CSS_SELECTOR, 'form[action="/shop"] .oe_search_box')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[class="btn oe_search_button btn btn-light"]')

    # Product elements
    PRODUCT_CARDS = (By.CSS_SELECTOR, "div.o_wsale_product_grid_wrapper")

    # Categories
    DESKS_CATEGORY = (By.CSS_SELECTOR, 'li[data-link-href="/shop/category/desks-1"] .btn span')
    FURNITURES_CATEGORY = (By.LINK_TEXT, "Furnitures")
