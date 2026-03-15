from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class cardLink:
    def __init__(self,browser):
        self._driver = browser
    def checkuot(self):
        self._driver.find_element(By.ID, 'checkout').click
