import pytest
from pages.home_page import HomePage


class TestHomePage:

    def test_home_page_loads_successfully(self, home_page):
        home_page.open_page()
        assert "testshop.qa-practice.com" in home_page.get_current_url()
        assert home_page.get_products_count() > 0

    def test_search_functionality(self, home_page):
        home_page.open_page()
        home_page.search_product("desk")
        current_url = home_page.get_current_url()
        assert "s=desk" in current_url or "search" in current_url

    def test_navigation_to_desks_category(self, home_page):
        home_page.open_page()
        home_page.click_desks_category()
        assert "desks" in home_page.get_current_url().lower()
