from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.desks_page import SalePage
from pages.cart_page import CustomerLogin


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    #options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)
