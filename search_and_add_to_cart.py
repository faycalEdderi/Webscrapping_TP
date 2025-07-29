from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

try:
    with open("credentials.txt", "r") as f:
        email = f.readline().strip()
        password = f.readline().strip()
except FileNotFoundError:
    exit()

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

try:
    driver.get("https://automationexercise.com/")
    time.sleep(4)

    try:
        driver.find_element(By.XPATH, "//button[@aria-label='Autoriser']").click()
        time.sleep(1)
    except:
        pass

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()
    time.sleep(3)

    try:
        product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/products']")))
        product_link.click()
        time.sleep(3)
    except:
        driver.execute_script("window.location.href = '/products';")
        time.sleep(3)

    search_input = wait.until(EC.presence_of_element_located((By.ID, "search_product")))
    search_input.clear()
    search_input.send_keys("dress")
    driver.find_element(By.ID, "submit_search").click()
    time.sleep(3)

    for i in range(2):
        add_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.add-to-cart")))
        if i >= len(add_buttons):
            break

        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_buttons[i])
            time.sleep(1)

            try:
                actions.move_to_element(add_buttons[i]).click().perform()
            except:
                driver.execute_script("arguments[0].click();", add_buttons[i])

            time.sleep(2)

            try:
                close_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.close-modal")))
                close_btn.click()
            except:
                pass
            time.sleep(1)

        except:
            driver.execute_script("arguments[0].click();", add_buttons[i])
            time.sleep(2)

    try:
        cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/view_cart']")))
        cart_link.click()
        time.sleep(3)
    except:
        driver.execute_script("window.location.href = '/view_cart';")
        time.sleep(3)

    cart_products = driver.find_elements(By.CSS_SELECTOR, "tr td.cart_quantity button")

    print(f"Nombre d'articles dans le panier : {len(cart_products)}")

finally:
    driver.quit()