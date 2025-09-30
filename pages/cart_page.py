from selenium.webdriver.support.wait import WebDriverWait
from utils import project_ec
from pages.base_page import BasePage
from locators import desks_page_locators as loc


class CustomerLogin(BasePage):
    page_url = '/customer/account/login'

    def fill_login_form(self, login, password):
        email_field = self.find(loc.email_field_locator)
        password_field = self.find(loc.password_field_locator)
        button = self.find(loc.button_locator)
        email_field.send_keys(login)
        password_field.send_keys(password)
        button.click()

    def check_error_alert_text_is(self, text):
        WebDriverWait(self.driver, 5).until(project_ec.text_is_not_empty_in_element(loc.error_locator))

        error_alert = self.driver.find_element(*loc.error_locator)
        assert error_alert.text == text
