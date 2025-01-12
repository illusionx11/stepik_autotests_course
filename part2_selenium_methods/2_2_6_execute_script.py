from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    
    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    y = calc(x)
    
    browser.execute_script("window.scrollBy(0, 100);")
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    radio = browser.find_element(By.ID, "robotsRule").click()
    
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
finally:
    time.sleep(30)
    browser.quit()
    
    
    