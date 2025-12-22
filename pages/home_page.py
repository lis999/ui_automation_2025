from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    page_url = ''

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators  # Import locators

    def wait_for_products(self):
        self.find(self.locators.PRODUCT_CARDS)

    def click_sign_in(self):
        self.click_element(self.locators.SIGN_IN_LINK)

    def click_contact_us(self):
        self.click_element(self.locators.CONTACT_LINK)

    def click_desks_category(self):
        self.click_element(self.locators.DESKS_CATEGORY)
        self.wait_for_url_contains("desks")

    def search_product(self, product_name: str):
        self.enter_text(self.locators.SEARCH_INPUT, product_name)
        self.click_element(self.locators.SEARCH_BUTTON)
        self.wait_for_url_contains("search")

    def get_products_count(self):
        return len(self.find_all(self.locators.PRODUCT_CARDS))

    def is_logo_displayed(self):
        return self.is_displayed(self.locators.LOGO)
