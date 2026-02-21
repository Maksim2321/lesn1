from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_form_submission():

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    waiter = WebDriverWait(driver, 15)
    waiter.until(EC.element_to_be_clickable((By.ID, "login-button")))
    driver.find_element(By.ID, "login-button").click()
    add_items=[
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Bolt T-Shirt"
    ]

    for item_name in add_items:
        add_button = waiter.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        )
    )

    shpopping_card = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    shpopping_card.click

    waiter.until(
    EC.element_to_be_clickable((By.ID, "checkout"))
    ).click

    name=driver.find_element(By.CSS_SELECTOR, "first-name").send_keys("Максим")
    last_name=driver.find_element(By.CSS_SELECTOR, "last-name").send_keys("Травников")
    code=driver.find_element(By.CSS_SELECTOR, "postal-code").send_keys("197372")

    total_price = waiter.until(
        EC.visibility_of_element_located(By.CSS_SELECTOR, "[class=summary_total_label]")
    )
    total_text = total_price.text

    assert total_text == "Итого: 58.29$", f"Ожидание: '58.29$', got '{total_text}'"

    driver.quit()
