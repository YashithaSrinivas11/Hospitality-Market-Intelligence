from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
import time

def selenium_booking_scraper():
    # 1. SETUP: Optimized for Docker environment
    print("⏳ Launching Chrome in a stable environment...")
    
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled") 
    
    try:
        driver = webdriver.Chrome(options=options)
        print("✅ SUCCESS: Chrome is live!")
    except Exception as e:
        print(f"❌ Still failing: {e}")
        return

    # 2. TARGET: New Delhi Hotels
    url = "https://www.booking.com/searchresults.en-gb.html?ss=New+Delhi&checkin=2025-04-01&checkout=2025-04-02&group_adults=2&no_rooms=1&group_children=0"
    
    try:
        driver.get(url)
        print("Connected! Waiting for data to load...")
        time.sleep(5) 

        # 3. FIND CARDS
        cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="property-card"]')
        
        if len(cards) == 0:
            print("Trying fallback selector...")
            cards = driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"]')

        print(f"Found {len(cards)} hotels! Scraping now...")

        # 4. SAVE DATA
        with open('selenium_booking_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Location', 'Price', 'Rating', 'Link'])
            
            for card in cards:
                try:
                    # NAME
                    name = card.find_element(By.CSS_SELECTOR, '[data-testid="title"]').text
                    
                    # LOCATION
                    try:
                        loc = card.find_element(By.CSS_SELECTOR, '[data-testid="address"]').text
                    except:
                        loc = "NA"
                        
                    # PRICE
                    try:
                        price = card.find_element(By.CSS_SELECTOR, '[data-testid="price-and-discounted-price"]').text
                        price = price.replace('₹', '').replace(',', '').strip()
                    except:
                        price = "NA"

                    # RATING
                    try:
                        rating = card.find_element(By.CSS_SELECTOR, '[data-testid="review-score"] div[aria-hidden="true"]').text
                    except:
                        rating = "NA"

                    # LINK
                    try:
                        link = card.find_element(By.CSS_SELECTOR, 'a[data-testid="title-link"]').get_attribute('href')
                    except:
                        link = "NA"
                    
                    writer.writerow([name, loc, price, rating, link])
                    print(f"Saved: {name}")
                    
                except Exception as e:
                    continue

        print("✅ Done! Check 'selenium_booking_data.csv'")

    except Exception as e:
        print(f"Critical Error: {e}")
        
    finally:
        driver.quit()

if __name__ == '__main__':
    selenium_booking_scraper()