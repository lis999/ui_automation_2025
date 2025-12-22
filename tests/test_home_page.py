import pytest
from pages.home_page import HomePage


class TestHomePage:

    def test_home_page_loads_successfully(self, home_page):
        home_page.open_page()
        home_page.wait_for_products()
        assert "testshop.qa-practice.com" in home_page.get_current_url()
        assert home_page.get_products_count() > 0

    def test_search_functionality(self, home_page):
        home_page.open_page()
        home_page.search_product("desk")
        current_url = home_page.get_current_url()
        assert "search=desk" in current_url

    def test_navigation_to_desks_category(self, home_page):
        home_page.open_page()
        home_page.click_desks_category()
        current_url = home_page.get_current_url()
        assert "shop/category/desks" in current_url
