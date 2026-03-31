from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


class CardLink:
    """
    Класс для работы со страницей корзины.
    Содержит методы для перехода на страницу корзины и оформления заказа.
    """
    
    def __init__(self, driver):
        """
        Инициализация объекта страницы корзины.
        
        driver: WebDriver - экземпляр драйвера Selenium
        """
        self._driver = driver
    
    @allure.step("Открыть страницу корзины")
    def get_card(self):
        """
        Переход на страницу корзины.
        
        Returns: None
        """
        self._driver.get("https://www.saucedemo.com/cart.html")
    
    @allure.step("Нажать кнопку оформления заказа")
    def checkout(self):
        """
        Нажатие кнопки 'Checkout' для перехода к оформлению заказа.
        
        Returns:
            None
        """
        self._driver.find_element(By.ID, 'checkout').click()
