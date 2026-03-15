from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class send_keys:
    def send_keys(self,browser):
        self._driver = browser
        self._driver.find_element(By.XPATH, "//span[text()='7']",).click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()
    
    def resault(self,browser):
         WebDriverWait(browser,50).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".screen"), "15")
    )