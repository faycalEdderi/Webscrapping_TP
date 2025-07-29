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

    driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()
    time.sleep(3)

    search_input = wait.until(EC.presence_of_element_located((By.ID, "search_product")))
    search_input.clear()
    search_input.send_keys("dress")
    driver.find_element(By.ID, "submit_search").click()
    time.sleep(3)

    product_blocks = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".single-products")))
    
    if len(product_blocks) < 2:
        exit()

    added_names = []

    for i in range(2):
        product_blocks = driver.find_elements(By.CSS_SELECTOR, ".single-products")
        if i >= len(product_blocks):
            break

        name_element = product_blocks[i].find_element(By.CSS_SELECTOR, "div.productinfo p")
        product_name = name_element.text

        if product_name in added_names:
            continue

        add_button = product_blocks[i].find_element(By.CSS_SELECTOR, "a.add-to-cart")

        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)
            time.sleep(1)
            actions.move_to_element(add_button).click().perform()
        except:
            driver.execute_script("arguments[0].click();", add_button)

        added_names.append(product_name)
        time.sleep(2)

        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.close-modal"))).click()
        except:
            pass
        time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']").click()
    time.sleep(3)

    cart_items = driver.find_elements(By.CSS_SELECTOR, "td.cart_description a")
    cart_names = [item.text for item in cart_items]

    if len(cart_names) >= 2 and cart_names[0] != cart_names[1]:
        pass
    else:
        pass

finally:
    driver.quit()