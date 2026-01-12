from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import os
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.desks_page import DesksPage
from pages.product_office_page import ProductOfficePage


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="run in headless mode",
    )

@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    is_headless = request.config.getoption("--headless") or os.getenv("CI")

    if is_headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    if not is_headless:
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def desks_page(driver):
    return DesksPage(driver)


@pytest.fixture()
def product_office_page(driver):
    return ProductOfficePage(driver)
