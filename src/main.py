from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
ATTENDANCE_URL = os.getenv("ATTENDANCE_URL")
USERNAME_ABSENSI = os.getenv("USERNAME_ABSENSI")
PASSWORD = os.getenv("PASSWORD")
DEFAULT_ACTIVITY = os.getenv("DEFAULT_ACTIVITY")

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Open the attendance page
    driver.get(ATTENDANCE_URL)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    print(USERNAME_ABSENSI)
    login_input = driver.find_element(By.ID, "login")
    password_input = driver.find_element(By.ID, "password")
    login_input.send_keys(USERNAME_ABSENSI)
    password_input.send_keys(PASSWORD)
    print("Silakan selesaikan reCAPTCHA secara manual dalam 30 detik...")
    time.sleep(20)

    submit_button = driver.find_element(By.ID, "submitBtn")
    submit_button.click()

    
    # Fill in the shift time (08:00 - 17:00 as an example)
    shift_input = driver.find_element(By.ID, "note")
    shift_input.clear()
    shift_input.send_keys(DEFAULT_ACTIVITY)

    # Select health condition (e.g., "Sehat" - Healthy)
    health_options = driver.find_elements(By.ID, "sehat")
    health_options.click()

    # Select work location (e.g., "Kantor" - Office)
    location_options = driver.find_elements(By.ID, "home")
    location_options.click()

    # Wait to see the result or submit the form
    time.sleep(20)

    print("Attendance submitted successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(2)
    driver.quit()