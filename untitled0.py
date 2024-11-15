from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
import time
import streamlit as st

def scrape_bond_yield():
    # Setting up Firefox options for headless mode
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")

    # Initialize the WebDriver for Firefox
    driver = webdriver.Firefox(options=firefox_options)

    try:
        # Navigate to the page
        driver.get("https://www.investing.com/rates-bonds/austria-10-year-bond-yield-historical-data")
        driver.set_window_size(1296, 768)
        time.sleep(2)  # Optional pause to allow the page to load fully
        
        # Wait and click on the menu arrow using WebDriverWait
        menu_arrow = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".historical-data-v2_selection-arrow__3mX7U > .flex-1"))
        )
        driver.execute_script("arguments[0].click();", menu_arrow)
        time.sleep(1)  # Optional pause to allow menu to open

        # Continue with the rest of your code logic...
        
    finally:
        driver.quit()

# Streamlit UI
st.title("Austria 10-Year Bond Yield Data Scraper")

if st.button("Scrape Data"):
    with st.spinner("Scraping data..."):
        result = scrape_bond_yield()
        st.write(result)

