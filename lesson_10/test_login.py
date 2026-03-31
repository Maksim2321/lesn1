from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
import pytest

from pages_login.authorization import auth
from pages_login.card_link import CardLink
from pages_login.add_to_card import add_card
from pages_login.information import Info


@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
class TestCheckout:
    """
    Тестовый класс для проверки процесса оформления заказа.
    """
    
    @pytest.fixture
    def browser(self):
        """
        Фикстура для инициализации и закрытия браузера.
        
        Returns:
            WebDriver: экземпляр драйвера
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()
    
    @allure.title("Проверка оформления заказа с заполнением всех данных")
    @allure.description("Тест проверяет процесс оформления заказа: переход в корзину, "
                       "заполнение информации о покупателе и получение итоговой суммы")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_checkout_process(self, browser):
        """
        Тест-кейс: Успешное оформление заказа.
        
        Шаги:
        1. Переход на страницу корзины
        2. Нажатие кнопки Checkout
        3. Заполнение информации о покупателе
        4. Получение итоговой суммы
        
        Ожидаемый результат: Итоговая сумма успешно получена
        """
        cart_page = CardLink(browser)
        checkout_page = Info(browser)
        
        with allure.step("Шаг 1: Открыть страницу корзины"):
            cart_page.get_card()
        
        with allure.step("Шаг 2: Нажать кнопку Checkout"):
            cart_page.checkout()
        
        with allure.step("Шаг 3: Заполнить информацию о покупателе"):
            checkout_page.info()
        
        with allure.step("Шаг 4: Получить итоговую сумму заказа"):
            total_amount = checkout_page.total()
            allure.attach(str(total_amount), "Итоговая сумма", allure.attachment_type.TEXT)
        
        with allure.step("Проверка: итоговая сумма должна быть положительным числом"):
            assert total_amount > 0, f"Итоговая сумма {total_amount} должна быть больше 0"
    
    @allure.title("Проверка получения итоговой суммы")
    @allure.description("Тест проверяет корректность получения итоговой суммы из элемента страницы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_total_amount_calculation(self, browser):
        """
        Тест-кейс: Проверка корректности получения итоговой суммы.
        
        Шаги:
        1. Переход на страницу корзины
        2. Нажатие кнопки Checkout
        3. Заполнение информации о покупателе
        4. Получение итоговой суммы
        
        Ожидаемый результат: Итоговая сумма получена в числовом формате
        """
        cart_page = CardLink(browser)
        checkout_page = Info(browser)
        
        with allure.step("Переход к оформлению заказа"):
            cart_page.get_card()
            cart_page.checkout()
            checkout_page.info()
        
        with allure.step("Получение итоговой суммы"):
            total_amount = checkout_page.total()
        
        with allure.step("Проверка типа возвращаемого значения"):
            assert isinstance(total_amount, int), f"Итоговая сумма должна быть int, получено {type(total_amount)}"