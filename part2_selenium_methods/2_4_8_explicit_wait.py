from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

url = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    btn = browser.find_element(By.CSS_SELECTOR, "button[id='book']").click()
    
    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    y = calc(x)
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
finally:
    time.sleep(20)
    browser.quit()
    