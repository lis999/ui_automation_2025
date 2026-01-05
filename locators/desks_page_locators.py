from selenium.webdriver.common.by import By


class DesksPageLocators:
    CUSTOMIZABLE_DESK = (By.CSS_SELECTOR, 'img[alt="Customizable Desk"]')
    ALL_DESKS = (By.CSS_SELECTOR, 'td[data-name="Product"]')
    CUSTOM_ROUND_BUTTON = (By.CSS_SELECTOR, '[id="1-7"]:first-of-type')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, 'i[class="oi oi-view-list"]')
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, 'i[class="fa fa-th-large"]')
    DESKS_CATEGORY_TITLE = (By.CSS_SELECTOR, 'span[class="d-inline-block"]')
    VIEW_CONTAINER = (By.CSS_SELECTOR, 'div[id="products_grid"]')
