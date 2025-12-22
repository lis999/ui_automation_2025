from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from time import sleep
from pages.home_page import HomePage
from pages.cart_page import CartPage


@pytest.fixture()
def driver():
    options = Options()
    #options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    sleep(3)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)
