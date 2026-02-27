import selenium.webdriver as webdriver
import time

def scrape_website(url):
    """Return the HTML content of the given URL using a Chrome webdriver.

    Selenium 4.4+ includes Selenium Manager, which automatically downloads
    and configures a compatible driver for the installed browser. This
    eliminates the need for a separate webdriver-manager dependency and
    prevents version mismatch errors.
    """

    print("launching browser...")
    options = webdriver.ChromeOptions()

    # Selenium will use Selenium Manager to handle the driver.
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        print("page loaded..")
        html = driver.page_source
        time.sleep(10)
        return html
    finally:
        driver.quit()