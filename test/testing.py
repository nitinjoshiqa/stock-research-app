from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Add headers to mimic a real browser
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

# Start Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# NSE Option Chain URL
url = "https://www.nseindia.com/option-chain"
driver.get(url)

# Wait for the table to load
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "opttbldata")))

# Extract table rows
rows = driver.find_elements(By.XPATH, "//table[contains(@class, 'opttbldata')]/tbody/tr")

option_data = []
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) > 10:  # Ensure valid row with data
        option_data.append({
            "Call OI": cols[0].text,
            "Call Change OI": cols[1].text,
            "Call Volume": cols[2].text,
            "Call LTP": cols[3].text,
            "Strike Price": cols[10].text,
            "Put LTP": cols[17].text,
            "Put Volume": cols[16].text,
            "Put Change OI": cols[15].text,
            "Put OI": cols[14].text
        })

# Convert to DataFrame
df = pd.DataFrame(option_data)
print(df.head())

# Save to CSV
df.to_csv("nse_option_chain.csv", index=False)
print("✅ Data saved to nse_option_chain.csv")

# Close the browser
driver.quit()
