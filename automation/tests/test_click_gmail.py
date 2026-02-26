from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_click_gmail():

    driver = webdriver.Chrome()
    driver.maximize_window()
# Open Google
    driver.get("https://www.google.com")
# Wait 2 seconds (page load)
    time.sleep(2)
# Click Gmail link (top right)
    gmail_link = driver.find_element(By.LINK_TEXT, "Gmail")
    gmail_link.click()
# Wait to observe
    time.sleep(3)
# Verify Gmail page loaded
    assert "Gmail" in driver.title
# Close browser
    driver.quit()
