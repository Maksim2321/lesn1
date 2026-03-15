
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class auth:
    def __init__(self,browser):
        self._driver = browser
        self._driver.get('http://www.saucedemo.com/')

    def test_shopping_flow(self):
        self._driver.find_element(By.ID, 'user-name')
        self._driver.send_keys('standard_user')
        self._driver.find_element(By.ID, 'password')
        self._driver.send_keys('secret_sauce', Keys.ENTER)