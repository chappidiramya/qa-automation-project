from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_open_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    print("Page title:", driver.title)
    time.sleep(2)
    driver.quit()
