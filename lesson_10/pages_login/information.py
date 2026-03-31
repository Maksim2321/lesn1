from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure

class Info:
    """
    Класс для работы со страницей оформления заказа.
    Содержит методы для заполнения информации о покупателе и получения итоговой суммы.
    """
    
    def __init__(self, browser):
        """
        Инициализация объекта страницы оформления заказа.
        
        Args:browser: WebDriver - экземпляр драйвера Selenium
        """
        self._driver = browser
    
    @allure.step("Заполнить информацию о покупателе")
    def info(self):
        """
        Заполнение формы с персональными данными покупателя:
        - Имя
        - Фамилия
        - Почтовый индекс
        
        После заполнения нажимает кнопку 'Continue'.
        
        Returns: None
        """
        self._driver.find_element(By.ID, 'first-name').send_keys('Максим')
        self._driver.find_element(By.ID, 'last-name').send_keys('Травников')
        self._driver.find_element(By.ID, 'postal-code').send_keys('12345')
        self._driver.find_element(By.ID, 'continue').click()
    
    @allure.step("Получить итоговую сумму заказа")
    def total(self):
        """
        Получение итоговой суммы заказа из элемента summary_total_label.
        
        Returns:int: Итоговая сумма заказа в виде целого числа
        """
        txt = self._driver.find_element(
        By.CLASS_NAME, 'summary_total_label').find_element(By.CSS_SELECTOR, "total-label").text
        return int(txt)