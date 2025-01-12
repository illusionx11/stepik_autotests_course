from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

url = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    
    inputs = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    inputs[0].send_keys("Ivan")
    inputs[1].send_keys("Ivanov")
    inputs[2].send_keys("Ivanov@ivan.com")
    
    upload = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '2_2_8.txt')
    print(file_path)
    upload.send_keys(file_path)
    
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
finally:
    time.sleep(20)
    browser.quit()