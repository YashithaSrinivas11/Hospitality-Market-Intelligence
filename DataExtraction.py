from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
import time
import random

def selenium_booking_scraper():
    # 1. SETUP: Launch a real Chrome browser
    print("⏳ Launching Chrome...")
    
    # Options to make us look human
    options = Options()
    # options.add_argument("--headless") 
    options.add_argument("--disable-blink-features=AutomationControlled") 
    
    driver = webdriver.Chrome(options=options)
    
    # 2. TARGET: New Delhi Hotels
    url = "https://www.booking.com/searchresults.en-gb.html?ss=New+Delhi&checkin=2025-04-01&checkout=2025-04-02&group_adults=2&no_rooms=1&group_children=0"
    
    try:
        driver.get(url)
        print("Connected! Waiting for data to load...")
        time.sleep(5) # Essential: Wait for JavaScript to finish loading

        # 3. FIND CARDS
        
    
        cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="property-card"]')
        
        if len(cards) == 0:
            print("If 0 then likely blocked or page structure changed. Trying a different selector")
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
                    print(f"Skipped a card due to error: {e}")
                    continue

        print("✅ Done! Check 'selenium_booking_data.csv'")

    except Exception as e:
        print(f"Critical Error: {e}")
        
    finally:
        # Close browser after 5 seconds
        time.sleep(5)
        driver.quit()

if __name__ == '__main__':
    selenium_booking_scraper()