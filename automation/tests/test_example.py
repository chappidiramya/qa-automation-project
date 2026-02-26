from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_example_page_title():

    # Start Chrome
    driver = webdriver.Chrome()

    # Open website
    driver.get("https://example.com")

    # Get page title
    title = driver.title
    print("Page Title is:", title)

    # Assertion (very important in automation)
    assert "Example Domain" in title

    # Wait 2 seconds (just to see browser)
    time.sleep(2)

    # Close browser
    driver.quit()
