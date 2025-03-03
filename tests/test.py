import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Initialize the WebDriver with ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Open Google
    driver.get('http://www.google.com/')
    time.sleep(5)  # Wait to see the page (for demonstration)

    # Find the search box using the new syntax
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('Made Agus Andi Gunawan')
    search_box.submit()
    time.sleep(5)  # Wait to see the results (for demonstration)

    print("Judul Halaman:", driver.title)
    driver.save_screenshot("google_search_result.png")  # Menyimpan screenshot
    print("Screenshot disimpan sebagai google_search_result.png")

    with open("google_search_result.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()