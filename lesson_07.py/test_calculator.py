from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from pages.OpenCalc import OpenCalc

def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    Calculator = OpenCalc(browser)
    Calculator.sec()
    Calculator.numbers()
    resault = Calculator.watier()

    assert resault == 15
