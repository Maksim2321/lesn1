
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


def test_form_sibmission():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    locator = driver.find_element(By.CSS_SELECTOR, "#delay")
    locator.send_keys(Keys.BACKSPACE)
    locator.send_keys("45")

    seven = driver.find_element(By.XPATH, "//span[text()='7']",).click()
    plus = driver.find_element(By.XPATH, "//span[text()='+']").click()
    eight = driver.find_element(By.XPATH, "//span[text()='8']").click()
    equals = driver.find_element(By.XPATH, "//span[text()='=']").click()

    waiter = WebDriverWait(driver,50).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,".screen"), "15")
    )
    resault = driver.find_element(By.CSS_SELECTOR, ".screen").text 

    print("результат:" + resault)

    driver.quit()