from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class cardLink:
    def __init__(self,driver):
        self._driver = driver
    def get_card(self):
        self._driver.get("https://www.saucedemo.com/cart.html") 
    def checkuot(self):
        self._driver.find_element(By.ID, 'checkout').click
