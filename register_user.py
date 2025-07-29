# register_user.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
import random

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://automationexercise.com/")
    time.sleep(5)

    try:
        consent_button = driver.find_element(By.XPATH, "//button[@aria-label='Autoriser']")
        consent_button.click()
        time.sleep(1)
    except Exception as e:
        print("Popup cookies non détectée ou déjà fermée")

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(2)

    email = f"testuser_{random.randint(1000, 9999)}@fakemail.com"
    name = f"testuser_{random.randint(1000, 9999)}"

    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
    time.sleep(3)

    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "days").send_keys("1")
    driver.find_element(By.ID, "months").send_keys("January")
    driver.find_element(By.ID, "years").send_keys("1990")
    driver.find_element(By.ID, "newsletter").click()
    driver.find_element(By.ID, "optin").click()

    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "company").send_keys("Test Co")
    driver.find_element(By.ID, "address1").send_keys("123 Main St")
    driver.find_element(By.ID, "country").send_keys("Canada")
    driver.find_element(By.ID, "state").send_keys("QC")
    driver.find_element(By.ID, "city").send_keys("Montreal")
    driver.find_element(By.ID, "zipcode").send_keys("H1A 1A1")
    driver.find_element(By.ID, "mobile_number").send_keys("5145551234")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)

    success_msg = driver.find_element(By.CLASS_NAME, "title").text
    if "ACCOUNT CREATED!" in success_msg:
        print("Compte créé avec succès !")
        print(f"Email utilisé : {email}")
        with open("credentials.txt", "w") as f:
            f.write(f"{email}\npassword123")
    else:
        print("Échec de création du compte")

finally:
    driver.quit()