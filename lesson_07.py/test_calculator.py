from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import main_page
from pages.keys import send_keys
from pages.waiter import send_waiter

def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    open_main_page = main_page(browser)
    
    send_waiter45 = send_waiter(browser)
    send_waiter45.send_waiter()

    send_78 = send_keys(browser)
    send_78.send_keys()
    to_be = send_78.resault()

    assert to_be == 15

    browser.quit()