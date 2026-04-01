import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from PagesShop.OpenShop import auth
from PagesShop.CardLink import CardLink
from PagesShop.AddCard import add_card
from PagesShop.Inf import InfoPage


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы браузера.
    """
    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    browser.maximize_window()
    yield browser
    browser.quit()


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка полного сценария покупки")
@allure.description("Тест проверяет полный путь пользователя: логин → добавление товара → оформление заказа")
def test_shoping_flow(driver):

    with allure.step("Авторизация"):
        authorize = auth(driver)
        authorize.get()
        authorize.login()

    with allure.step("Добавление товаров в корзину"):
        addToCard = add_card(driver)
        addToCard.add_to_card()
        addToCard.to_card_link()

    with allure.step("Переход к оформлению"):
        card_link = CardLink(driver)
        card_link.get_card()
        card_link.checkout()

    with allure.step("Заполнение информации"):
        inform = InfoPage(driver)
        inform.fill_info("Максим", "Гравников", "12345")
        inform.continue_checkout()

    with allure.step("Получение итоговой суммы"):
        total = inform.get_total()

    with allure.step("Проверка результата"):
        assert total == 58 