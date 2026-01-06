from time import sleep


class TestProductOfficePage:

    def test_product_office_page_opens(self, product_office_page):
        product_office_page.open_page()
        product_name = product_office_page.get_product_category_name()
        assert "Office Design Software" in product_name

    def test_product_price_is_correct(self, product_office_page):
        product_office_page.open_page()
        product_price = product_office_page.get_product_category_price()
        assert float(product_price) == 280.00

    def test_item_added_to_cart(self, product_office_page):
        product_office_page.open_page()
        sleep(5)
        cart_before_update = int(product_office_page.check_quantity_in_cart() or 0)
        product_office_page.add_item_to_cart()
        sleep(5)
        product_office_page.wait_cart_updated(cart_before_update)
        items_in_cart = int(product_office_page.check_quantity_in_cart() or 0)
        assert items_in_cart > cart_before_update
