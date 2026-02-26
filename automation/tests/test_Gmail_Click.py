from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

def test_Gmail_Click():
driver = webdriver.Chrome()
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
  
