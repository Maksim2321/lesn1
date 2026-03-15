from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class total:
    def __init__(self,browser):
       self._driver = browser
    def total_amount(self):
        txt = self._driver.find_element(
        By.CLASS_NAME, 'summary_total_label').find_element(By.CSS_SELECTOR, "total-label").text
        return int(txt)