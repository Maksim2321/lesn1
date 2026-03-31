
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure

class auth:
    def __init__(self, browser):
        """
        :param browser: экземпляр WebDriver
        :type browser: WebDriver
        """
        self.driver = browser

    @allure.step("Открыть страницу авторизации")
    def get(self) -> None:
        """
        Открывает страницу сайта

        :return: None
        """
        self.driver.get('http://www.saucedemo.com/')

    @allure.step("Выполнить логин")
    def login(self) -> None:
        """
        Выполняет вход в систему

        :return: None
        """
        username_field = self.driver.find_element(By.ID, 'user-name')
        username_field.send_keys('standard_user')

        password = self.driver.find_element(By.ID, 'password')
        password.send_keys('secret_sauce', Keys.ENTER)