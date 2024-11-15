import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
import time

# Function to perform the Selenium task
def scrape_bond_yield():
    # Setting up Firefox options for headless mode
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")  # Run Firefox in headless mode

    # Initialize the WebDriver for Firefox
    driver = webdriver.Firefox(options=firefox_options)

    try:
        # Navigating to the page
        driver.get("https://www.investing.com/rates-bonds/austria-10-year-bond-yield-historical-data")
        driver.set_window_size(1296, 768)
        time.sleep(2)  # Optional pause to allow the page to load fully
        
        # Accepting cookies if the accept button is present
        try:
            accept_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_button.click()
        except Exception as e:
            st.write("No cookies accept button found:", e)
        
        # Scrolling to the required position
        driver.execute_script("window.scrollTo(0, 358.6666564941406)")
        time.sleep(1)  # Optional pause after scrolling

        # Handle potential modal or iframe blocking the interaction
        try:
            # Wait for any potential modal to disappear
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.ID, "lightbox-iframe-2b0f8da3-1006-4ea7-b4ea-456c1302759c"))
            )
        except Exception as e:
            st.write("Modal overlay might still be present:", e)
        
        # Attempt to click elements with JavaScript if standard clicks are intercepted
        menu_arrow = driver.find_element(By.CSS_SELECTOR, ".historical-data-v2_selection-arrow__3mX7U > .flex-1")
        driver.execute_script("arguments[0].click();", menu_arrow)
        time.sleep(1)  # Optional pause to allow menu to open
        
        menu_item = driver.find_element(By.CSS_SELECTOR, ".historical-data-v2_menu-row__oRAlf:nth-child(2) > .historical-data-v2_menu-row-text__ZgtVH")
        driver.execute_script("arguments[0].click();", menu_item)
        time.sleep(2)  # Optional pause to allow data to load
        
        # Extracting and printing the value
        rr_value = driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(3)").text
        return f"RR Value: {rr_value}"

    finally:
        # Closing the driver after execution
        driver.quit()

# Streamlit UI
st.title("Austria 10-Year Bond Yield Data Scraper")

if st.button("Scrape Data"):
    with st.spinner("Scraping data..."):
        result = scrape_bond_yield()
        st.write(result)

