import time

from selenium.webdriver.common.by import By

from conftest import browser


def test_locators(browser):
    browser.get("https://www.saucedemo.com/")
    username = browser.find_element(By.ID, "user-name")
    password = browser.find_element(By.NAME, "password")
    login_btn = browser.find_element(By.CLASS_NAME, "submit-button")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()
    image = browser.find_element(By.TAG_NAME, "img")

    burger_menu = browser.find_element(By.ID, "react-burger-menu-btn")
    burger_menu.click()
    time.sleep(1)
    link_text = browser.find_element(By.LINK_TEXT, "All Items")
    prt_link_text = browser.find_element(By.PARTIAL_LINK_TEXT, "Reset App")
    xpath_attribute = browser.find_element(By.XPATH, "//button[@type='button']")
    xpath_text = browser.find_element(By.XPATH, "//button[text()='Close Menu']")
    xpath_text.click()
    xpath_attribute_part = browser.find_element(By.XPATH, "//div[contains(@class, 'inventory_item')]")
    xpath_text_part = browser.find_element(By.XPATH, "//div[contains(text(), 'A red light')]")
    xpath_ancestor = browser.find_element(By.XPATH, "//button[@type='button']/ancestor::div")
    xpath_descendant = browser.find_element(By.XPATH, "//div[contains(@class, 'inventory_item')]/descendant::button")
    xpath_following = browser.find_element(By.XPATH, "//div[contains(@class, 'inventory_item')]/following::button")
    xpath_parent = browser.find_element(By.XPATH, "//div[contains(text(), 'A red light')]/parent::*")
    xpath_preceding = browser.find_element(By.XPATH, "//div[contains(text(), 'A red light')]/preceding::button")
    xpath_and = browser.find_element(By.XPATH, "//button[@type='button' and text()='Open Menu']")

    css_class = browser.find_element(By.CSS_SELECTOR, ".btn")
    css_class_class = browser.find_element(By.CSS_SELECTOR, ".btn.btn_primary")
    css_class_child = browser.find_element(By.CSS_SELECTOR, ".pricebar .btn")
    css_id = browser.find_element(By.CSS_SELECTOR, "#shopping_cart_container")
    css_tag = browser.find_element(By.CSS_SELECTOR, "button")
    css_tag_class = browser.find_element(By.CSS_SELECTOR, "div.inventory_item_img")
    css_attribute = browser.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    css_part_attribute = browser.find_element(By.CSS_SELECTOR, "[aria-label~=View]")
    css_beginning_attribute = browser.find_element(By.CSS_SELECTOR, "[data-test|=item]")
    css_beginning_attribute_2 = browser.find_element(By.CSS_SELECTOR, "[data-test^=item]")
    css_ending_attribute = browser.find_element(By.CSS_SELECTOR, "[data-test$=link]")
    css_contains_attribute = browser.find_element(By.CSS_SELECTOR, "[data-test*=title]")





