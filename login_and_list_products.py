from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://www.saucedemo.com")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print("Liste des produits disponibles :")
    for product in products:
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        print(f"- {name}")

finally:
    driver.quit()