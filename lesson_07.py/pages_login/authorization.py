
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class auth:
    def __init__(self,browser):
        self._driver = browser
    def get(self):
        self._driver.get('http://www.saucedemo.com/')

    def login(self):
        username_field = self._driver.find_element(By.ID, 'user-name')
        username_field.send_keys('standard_user')
        password = self._driver.find_element(By.ID, 'password')
        password.send_keys('secret_sauce', Keys.ENTER)