from pages.base_page import BasePage
from locators.product_office_locators import ProductOfficeLocators


class ProductOfficePage(BasePage):
    page_url = 'shop/furn-9999-office-design-software-7?category=9'

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductOfficeLocators

    def get_product_category_name(self):
        return self.get_text(self.locators.PRODUCT_CATEGORY_NAME)

    def get_product_category_price(self):
        return self.get_text(self.locators.OFFICE_SOFTWARE_PRICE)

    def add_item_to_cart(self):
        return self.click_element(self.locators.ADD_TO_CART_BUTTON)

    def check_quantity_in_cart(self):
        return self.get_text(self.locators.NUMBER_ITEMS_CART)

    def wait_cart_updated(self, cart_before_update: int):
        self.wait.until(
            lambda driver: int(self.check_quantity_in_cart() or 0) > cart_before_update
        )
