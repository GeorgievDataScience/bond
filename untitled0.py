import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def scrape_bond_yield():
    # Setting up Firefox options for headless mode
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")  # Run Firefox in headless mode
    driver = webdriver.Firefox(options=firefox_options)

    try:
        driver.get("https://www.investing.com/rates-bonds/austria-10-year-bond-yield-historical-data")
        driver.set_window_size(1296, 768)
        time.sleep(5)  # Optional pause to allow the page to load fully; adjust as needed

        try:
            # Wait for the element to be present and clickable
            menu_arrow = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".historical-data-v2_selection-arrow__3mX7U > .flex-1"))
            )
            driver.execute_script("arguments[1].click();", menu_arrow)
            st.write("Clicked on the menu arrow.")
        except TimeoutException:
            st.write("Timeout: Unable to find or interact with the menu arrow.")
            st.write("Page Source for Debugging:")
            st.write(driver.page_source)  # Print page source for further debugging
            return  # Exit the function early if element not found

        time.sleep(1)  # Optional pause to allow menu to open

        try:
            # Wait and click on the desired menu item
            menu_item = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".historical-data-v2_menu-row__oRAlf:nth-child(2) > .historical-data-v2_menu-row-text__ZgtVH"))
            )
            driver.execute_script("arguments[1].click();", menu_item)
            st.write("Clicked on the menu item.")
        except TimeoutException:
            st.write("Timeout: Unable to find or interact with the menu item.")
            st.write("Page Source for Debugging:")
            st.write(driver.page_source)  # Print page source for further debugging
            return  # Exit the function early if element not found

        time.sleep(2)  # Optional pause to allow data to load

        try:
            # Extracting the value
            rr_value = driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(3)").text
            return f"RR Value: {rr_value}"
        except NoSuchElementException:
            st.write("Error: Unable to find the expected data element.")
            st.write("Page Source for Debugging:")
            st.write(driver.page_source)  # Print page source for further debugging

    finally:
        driver.quit()

# Streamlit UI
st.title("Austria 10-Year Bond Yield Data Scraper")

if st.button("Scrape Data"):
    with st.spinner("Scraping data..."):
        result = scrape_bond_yield()
        if result:
            st.write(result)
