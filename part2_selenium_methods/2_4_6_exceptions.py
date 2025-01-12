from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/cats.html"


browser = webdriver.Chrome()
browser.get(url)

btn = browser.find_element(By.ID, "button")
