import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

def scrape_bond_yield():
    # Setting up Firefox options for headless mode
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")

    driver = webdriver.Firefox(options=firefox_options)

    try:
        driver.get("https://www.investing.com/rates-bonds/austria-10-year-bond-yield-historical-data")
        driver.set_window_size(1296, 768)
        time.sleep(5)  # Allow time for page to load fully; adjust as needed

        try:
            menu_arrow = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".historical-data-v2_selection-arrow__3mX7U > .flex-1"))
            )
            driver.execute_script("arguments[0].click();", menu_arrow)
        except TimeoutException:
            st.write("Timeout: Unable to find or interact with the menu arrow.")
            st.write(driver.page_source)  # Optional: print page source for debugging

        # Further interactions...

    finally:
        driver.quit()

st.title("Austria 10-Year Bond Yield Data Scraper")

if st.button("Scrape Data"):
    with st.spinner("Scraping data..."):
        scrape_bond_yield()

