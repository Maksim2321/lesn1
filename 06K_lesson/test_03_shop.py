from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
waiter = WebDriverWait(driver,15)

driver.get("https://www.saucedemo.com/")

user = driver.find_element(By.CSS_SELECTOR, "[placeholder=Имя пользователя]").send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, "[type=password]").send_keys("secret_sauce")
login = driver.find_element(By.CSS_SELECTOR, "[id=login-button]")
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
