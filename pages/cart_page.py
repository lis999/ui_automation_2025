from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    page_url = 'shop/cart'

    def check_page_header_title_is(self, text):
        header_title = self.find(header_title_loc)
        assert header_title.text == text