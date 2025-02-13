from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse

# Set up your WebDriver (adjust the path to your chromedriver)
driver = webdriver.Chrome()

# Navigate to IMDb and log in manually
driver.get("https://www.imdb.com/registration/signin")
print("Log in to IMDb, then press Enter here...")
input()  # Wait for you to complete login manually

# Read movie titles from a text file (one title per line)
with open("movies.txt", "r", encoding="utf-8") as file:
    movies = [line.strip() for line in file if line.strip()]

wait = WebDriverWait(driver, 10)


for movie in movies:
    try:
        # URL-encode the movie title and search
        query = urllib.parse.quote(movie)
        search_url = f"https://www.imdb.com/find?q={query}"
        driver.get(search_url)
        time.sleep(2)  # Wait for results to load

        # Click on the first search result (you might need to adjust the selector if IMDb changes their layout)
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[contains(@class, 'find-title-result')]//a[contains(@class, 'ipc-metadata-list-summary-item__t')]")
        ))        
        element.click()
        time.sleep(2)

        # Look for the "Add to Watchlist" button. This selector might need adjustments!
        # Note: For custom lists, you'd need to simulate clicking the "Add to" dropdown and then selecting your list.
        try:
            watchlist_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='poster-watchlist-ribbon-add']"))
            )

            # Scroll the button into view
            driver.execute_script("arguments[0].scrollIntoView(true);", watchlist_button)
            time.sleep(1)  # Give time for any animations or overlays to adjust

            # Use JavaScript to click the element
            driver.execute_script("arguments[0].click();", watchlist_button)
            print(f"Added '{movie}' to your watchlist.")
        except Exception as inner_err:
            print(f"Could not add '{movie}': {inner_err}")
        time.sleep(1)
    except Exception as e:
        print(f"Error processing '{movie}': {e}")

driver.quit()