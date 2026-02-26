from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def test_open_google():

    # Optional: run browser in headless mode
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment to run without opening browser

    # Start Chrome browser
    driver = webdriver.Chrome(options=chrome_options)

    # Open website
    driver.get("https://www.google.com")

    # Print page title
    print("Page title is:", driver.title)

    # Wait 3 seconds (just for demo)
    time.sleep(3)

    # Close browser
    driver.quit()
