from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL = "https://kqxntj5wiqk3w7s2zgk6dc.streamlit.app/"

def visit_app():
    print("Starting headless Chrome...")

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        print(f"Visiting: {APP_URL}")
        driver.get(APP_URL)

        # Warten, damit die WebSocket-Verbindung aufgebaut wird
        time.sleep(15)

        print("Page loaded.")
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    visit_app()
