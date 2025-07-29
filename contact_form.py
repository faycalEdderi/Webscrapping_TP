from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://automationexercise.com/")
    time.sleep(4)

    try:
        driver.find_element(By.XPATH, "//button[@aria-label='Autoriser']").click()
        time.sleep(1)
    except:
        pass

    driver.find_element(By.LINK_TEXT, "Contact us").click()
    time.sleep(3)

    driver.find_element(By.NAME, "name").send_keys("John Doe")
    driver.find_element(By.NAME, "email").send_keys("john@example.com")
    driver.find_element(By.NAME, "subject").send_keys("Support Request")
    driver.find_element(By.NAME, "message").send_keys("Hello, this is a test message from Selenium automation.")

    test_file = "test_upload.txt"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("Fichier de test pour upload via Selenium.")

    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(os.path.abspath(test_file))
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "input[data-qa='submit-button']").click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)

    success_msg = driver.find_element(By.CSS_SELECTOR, "div.status.alert.alert-success").text
    if "Success! Your details have been submitted successfully." in success_msg:
        print("Formulaire envoyé avec succès !")
    else:
        print("Échec d'envoi du formulaire")

    driver.save_screenshot("contact_success.png")

finally:
    driver.quit()
    if os.path.exists(test_file):
        os.remove(test_file)