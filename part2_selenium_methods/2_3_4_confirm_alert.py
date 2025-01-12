from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    
    alert_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    alert = browser.switch_to.alert
    alert.accept()
    
    time.sleep(0.2)
    
    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    y = calc(x)
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
finally:
    time.sleep(20)
    browser.quit()
    
    
    