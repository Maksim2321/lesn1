from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

push_log = driver.find_element(By.TAG_NAME, "input")
push_log.click()
push_log.send_keys("Sky")

push_log.clear()

push_log.send_keys("Pro")

driver.quit()