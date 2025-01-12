from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    
    result = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
    print("result is ", result)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))
    
    btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
finally:
    time.sleep(30)
    browser.quit()