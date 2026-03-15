from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages_login.authorization import auth
from pages_login.card_link import cardLink
from pages_login.add_to_card import add_card
from pages_login.information import info
from pages_login.total import total

def test_shopping_flow():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    authorize = auth(browser)
    authorize.test_shopping_flow()

    addToCard = add_card(browser)
    addToCard.add_to_card()
    addToCard.to_card_link()

    card_link = cardLink(browser)
    card_link.checkuot()

    inform = info(browser)
    inform.info()

    ttl = total(browser)
    txt = ttl.total_amount()



    assert txt == 58.29, (
        f"Итоговая сумма должна быть $58.29, но указана {txt}"
    )
    browser.quit()