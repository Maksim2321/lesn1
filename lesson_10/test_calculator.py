from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pytest
import allure

from pages.OpenCalc import OpenCalc


@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 15)
    ],
)
@allure.title("Тестирование калькулятора: {num1} {operation} {num2} "
              "= {expected_result}")
@allure.description("Тест проверяет корректность работу калькулятора "
                    "с различными операциями.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_flow(driver, num1, operation,
                         num2, expected_result, delay):
    """
    Тест проверяет работу калькулятора с различными операциями.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :param num1: str — первое число для операции.
    :param operation: str — операция (+).
    :param num2: str — второе число для операции.
    :param expected_result: str — ожидаемый результат операции.
    :param delay: int — задержка в секундах для выполнения операции.
    """
    main_page = OpenCalc(driver)

    with allure.step("Открытие страницы калькулятора"):
        main_page.open()

    with allure.step(f"Установка задержки {delay} секунд"):
        main_page.set_delay(delay)

    with allure.step(f"Нажатие кнопок: {num1}, {operation}, {num2}, '='"):
        main_page.click_buttons([num1, operation, num2, "="])

    with allure.step(f"Ожидание результата {expected_result}"):
        main_page.wait_for_result(expected_result, delay)

    with allure.step("Проверка результата"):
        assert main_page.get_result() == expected_result, \
            (f"Ожидаемый результат: {expected_result}, "
             f"но получен: {main_page.get_result()}")
