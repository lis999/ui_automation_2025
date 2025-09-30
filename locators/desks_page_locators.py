from selenium.webdriver.common.by import By


email_field_locator = (By.CSS_SELECTOR, 'input[type="email"]')
password_field_locator = (By.CSS_SELECTOR, 'input[type="password"]')
button_locator = (By.XPATH, "//button[@id='send2']")
error_locator = (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
