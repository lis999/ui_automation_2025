from pages.base_page import BasePage
from locators.desks_page_locators import DesksPageLocators


class DesksPage(BasePage):
    page_url = 'shop/category/desks-1'

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DesksPageLocators

    def wait_for_desk_cards(self):
        self.find(self.locators.ALL_DESKS)

    def get_desks_count(self):
        return len(self.find_all(self.locators.ALL_DESKS))

    def get_category_title(self):
        return self.get_text(self.locators.DESKS_CATEGORY_TITLE)

    def switch_to_list_view(self):
        self.click_element(self.locators.LIST_VIEW_BUTTON)

    def switch_to_grid_view(self):
        self.click_element(self.locators.GRID_VIEW_BUTTON)

    def get_view_container_classes(self):
        return self.find(self.locators.VIEW_CONTAINER).get_attribute("class")

    def wait_for_view_change(self, previous_classes: str):
        self.wait.until(
            lambda driver: self.get_view_container_classes() != previous_classes
        )
