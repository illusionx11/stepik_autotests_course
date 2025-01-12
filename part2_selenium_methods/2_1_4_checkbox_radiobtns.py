from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    x_element = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    captcha = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    captcha.click()
    
    robots = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robots.click()
    
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()