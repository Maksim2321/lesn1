from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class send_waiter:
    def send_waiter(self,driver):
        self._driver = driver
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")