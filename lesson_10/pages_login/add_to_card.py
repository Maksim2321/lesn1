from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure


class add_card:
    def __init__(self, driver):
        """
        :param driver: WebDriver
        :type driver: WebDriver
        """
        self._driver = driver

    @allure.step("Добавить товары в корзину")
    def add_to_card(self) -> None:
        """
        Добавляет товары в корзину

        :return: None
        """
        WebDriverWait(self._driver, 10).until(EC.url_contains('/inventory.html'))

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"))
        ).click()

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
        ).click()

        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']"))
        ).click()

    @allure.step("Перейти в корзину")
    def to_card_link(self) -> None:
        """
        Переходит в корзину

        :return: None
        """
        self._driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()