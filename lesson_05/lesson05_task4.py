from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/login")

push_log = driver.find_element(By.ID, "username").send_keys("tomsmith")

push_log = driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

push_log = driver.find_element(By.CLASS_NAME, "radius").click()

green_text = driver.find_element(By.CSS_SELECTOR, "div.flash.success").text


print(green_text)

driver.quit()
