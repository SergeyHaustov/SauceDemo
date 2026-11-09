from selenium.webdriver.common.by import By

from conftest import browser


def test_cart(browser):
    browser.get("https://www.saucedemo.com/")
    username = browser.find_element(By.ID, "user-name")
    password = browser.find_element(By.NAME, "password")
    login_btn = browser.find_element(By.CLASS_NAME, "submit-button")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()

    bike_light_btn = browser.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bike-light']")
    bike_light_btn.click()
    shopping_cart = browser.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    shopping_cart.click()
    item_name = browser.find_element(By.CSS_SELECTOR, ".inventory_item_name")
    item_price = browser.find_element(By.CSS_SELECTOR, ".inventory_item_price")
    assert item_name.text == "Sauce Labs Bike Light" and item_price.text == "$9.99"

