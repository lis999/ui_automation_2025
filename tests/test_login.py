from selenium import webdriver
from selenium.webdriver.common.by import By


def test_incorrect_login(driver):
    driver.get('https://magento.softwaretestingboard.com/customer/account/login')
    email_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')
    login_button = driver.find_element(By.ID, 'send2')
    error_alert = driver.find_element(By.CSS_Selector, 'send2')

