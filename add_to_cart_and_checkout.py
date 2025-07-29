from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://www.saucedemo.com")
    time.sleep(1)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    add_buttons[0].click()
    time.sleep(1)
    add_buttons[1].click()
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)

    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)

    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("75001")
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    driver.find_element(By.ID, "finish").click()
    time.sleep(2)

    success_msg = driver.find_element(By.CLASS_NAME, "complete-header").text
    if "THANK YOU FOR YOUR ORDER" in success_msg.upper():
        print("Commande réussie !")
    else:
        print("Échec : Message non trouvé")

    driver.save_screenshot("checkout_confirmation.png")
    print("Capture d'écran sauvegardée : checkout_confirmation.png")

finally:
    driver.quit()