from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class info:
    def __init__(self,browser):
        self._driver = browser
    def info(self):
        self._driver.find_element(By.ID, 'first-name').send_keys('Мария')
        self._driver.find_element(By.ID, 'last-name').send_keys('Французова')
        self._driver.find_element(By.ID, 'postal-code').send_keys('12345')
        self._driver.find_element(By.ID, 'continue').click()