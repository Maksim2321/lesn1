import allure
from selenium.webdriver.common.by import By


class InfoPage:
    """
    Класс для работы с страницей ввода информации.
    """

    def __init__(self, browser):
        """
        Инициализация страницы.

        :param browser: WebDriver
        :type browser: selenium.webdriver
        """
        self._driver = browser

    @allure.step("Заполнить данные: имя={first_name}, фамилия={last_name}, индекс={postal_code}")
    def fill_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму пользователя.

        :param first_name: Имя пользователя
        :type first_name: str
        :param last_name: Фамилия пользователя
        :type last_name: str
        :param postal_code: Почтовый индекс
        :type postal_code: str
        :return: None
        """
        self._driver.find_element(By.ID, 'first-name').send_keys(first_name)
        self._driver.find_element(By.ID, 'last-name').send_keys(last_name)
        self._driver.find_element(By.ID, 'postal-code').send_keys(postal_code)

    @allure.step("Продолжить оформление заказа")
    def continue_checkout(self) -> None:
        """
        Нажимает кнопку Continue.

        :return: None
        """
        self._driver.find_element(By.ID, 'continue').click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> int:
        """
        Получает итоговую сумму заказа.

        :return: Итоговая сумма
        :rtype: int
        """
        txt = self._driver.find_element(
            By.CLASS_NAME, 'summary_total_label'
        ).text

        return int(float(txt.split("$")[1]))