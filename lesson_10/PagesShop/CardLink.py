import allure
from selenium.webdriver.common.by import By


class CardLink:
    """
    Класс для работы с страницей корзины.
    """

    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: WebDriver
        :type driver: selenium.webdriver
        """
        self._driver = driver

    @allure.step("Открыть страницу корзины")
    def get_card(self) -> None:
        """
        Открывает страницу корзины.

        :return: None
        """
        self._driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Нажать кнопку Checkout")
    def checkout(self) -> None:
        """
        Нажимает кнопку Checkout.

        :return: None
        """
        self._driver.find_element(By.ID, 'checkout').click()
