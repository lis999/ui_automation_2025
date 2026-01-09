from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):
    page_url = 'shop/cart'

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocators

    def click_search(self):
        self.click_element(self.locators.SEARCH_BUTTON)

    def is_search_input_visible(self):
        return self.is_displayed(self.locators.SEARCH_FIELD)

    def get_order_overview_text(self):
        return self.get_text(self.locators.ORDER_OVERVIEW)

    def get_cart_quantity(self):
        text = self.get_text(self.locators.CART_ICON_COUNT).strip()
        return int(text) if text else 0
