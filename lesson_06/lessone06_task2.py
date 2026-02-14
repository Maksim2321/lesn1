
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver,10)

driver.get("http://uitestingplayground.com/textinput")


button_name = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
button_name.click
button_name.send_keys("SkyPro")

blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

waiter = WebDriverWait(driver,10)
waiter.until(
    EC.text_to_be_present_in_element( (By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
)

print( driver.find_element(By.CSS_SELECTOR, "#updatingButton").text )

driver.quit()
