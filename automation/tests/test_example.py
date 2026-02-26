from selenium import webdriver
import time

def test_example_page_title():

    driver = webdriver.Chrome()
    driver.get("https://example.com")

    title = driver.title
    print("Page Title:", title)

    assert "Example Domain" in title

    time.sleep(2)
    driver.quit()
