class TestDesksPage:

    def test_desks_category_page_opens(self, desks_page):
        desks_page.open_page()
        assert "desks-1" in desks_page.get_current_url()

    def test_desks_category_has_desks(self, desks_page):
        desks_page.open_page()
        desks_page.wait_for_desk_cards()
        assert desks_page.get_desks_count() > 0

    def test_desks_category_title(self, desks_page):
        desks_page.open_page()
        title = desks_page.get_category_title()
        assert "Desks" in title

    def test_switch_between_grid_and_list_view(self, desks_page):
        desks_page.open_page()

        # Switch to list view
        previous_classes = desks_page.get_view_container_classes()
        desks_page.switch_to_list_view()
        desks_page.wait_for_view_change(previous_classes)
        classes_after_list = desks_page.get_view_container_classes()
        assert "o_wsale_layout_list" in classes_after_list

        # Switch back to grid view
        previous_classes = classes_after_list
        desks_page.switch_to_grid_view()
        desks_page.wait_for_view_change(previous_classes)
        classes_after_grid = desks_page.get_view_container_classes()
        assert "o_wsale_layout_list" not in classes_after_grid
