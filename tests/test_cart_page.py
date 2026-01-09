class TestCartPage:

    def test_cart_page_loaded(self, cart_page):
        cart_page.open_page()
        cart_url = cart_page.get_current_url()
        assert "cart" in cart_url

        overview_text = cart_page.get_order_overview_text()
        assert "Order overview" in overview_text

    def test_cart_is_empty(self, cart_page):
        cart_page.open_page()
        items_in_cart = cart_page.get_cart_quantity()
        assert items_in_cart == 0

        overview_status = cart_page.get_order_overview_text()
        assert "cart is empty" in overview_status

    def test_search_is_available(self, cart_page):
        cart_page.open_page()
        cart_page.click_search()
        assert cart_page.is_search_input_visible()
