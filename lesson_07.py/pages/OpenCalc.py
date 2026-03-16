from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class OpenCalc:
    def __init__(self,driver):
        #зайти на сайт
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)

    def sec(self):
        #добавить 45 сек
        number = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        number.send_keys(Keys.BACKSPACE)
        number.send_keys("45")


    def numbers(self):
        #нажать на цифры+ожидание
        self._driver.find_element(By.XPATH, "//span[text()='7']",).click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()
    def watier(self):
        #ожидание+результат
        waiter = WebDriverWait(self._driver,50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,".screen"), "15")
        )
        txt = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
    
    