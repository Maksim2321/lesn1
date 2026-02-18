
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

waiter = WebDriverWait(driver,15)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = driver.find_element(By.CSS_SELECTOR, "[name=first-name]").send_keys("Иван")
last_name = driver.find_element(By.CSS_SELECTOR, "[name=last-name]").send_keys("Петров")
address = driver.find_element(By.CSS_SELECTOR, "[name=address]").send_keys("Ленина, 55-3")
zip_code = driver.find_element(By.CSS_SELECTOR, "[name=zip-code]")
city = driver.find_element(By.CSS_SELECTOR, "[name=city]").send_keys("Москва")
country = driver.find_element(By.CSS_SELECTOR, "[name=country]").send_keys("Россия")
e_mail = driver.find_element(By.CSS_SELECTOR, "[name=e-mail]").send_keys("test@skypro.com")
phone = driver.find_element(By.CSS_SELECTOR, "[name=phone]").send_keys("+7985899998787")
job_position = driver.find_element(By.CSS_SELECTOR, "[name=job-position]").send_keys("QA")
company = driver.find_element(By.CSS_SELECTOR, "[name=company]").send_keys("SkyPro")

button = driver.find_element(By.CLASS_NAME, "btn-outline-primary").click()
waiter.until(lambda d: "data-types-submitted.html" in d.current_url)

zip_div = driver.find_element(By.ID, "zip-code")
assert "alert-danger" in zip_div.get_attribute("class")

fields = [
    "first_name",
    "last_name",
    "address",
    "city",
    "country",
    "e_mail",
    "phone",
    "job_position",
    "company",
]
for fields_id in fields:
    field_element= driver.find_element(By.ID, fields_id)
    assert "alert-succes" in field_element.get_attribute("class")

driver(quit)