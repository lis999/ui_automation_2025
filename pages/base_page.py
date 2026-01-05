from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple


Locator = Tuple[str, str]

class BasePage:
    base_url = 'http://testshop.qa-practice.com/'
    page_url = None

    def __init__(self, driver: WebDriver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_page(self):
        if self.page_url is None:
            raise NotImplementedError('Page can not be opened for this page class')
        self.driver.get(f'{self.base_url}{self.page_url}')

    def find(self, locator: Locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator: Locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_element(self, locator: Locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator: Locator, text: str):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_displayed(self, locator: Locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, text: str):
        self.wait.until(EC.url_contains(text))
