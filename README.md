# 🏨 Dynamic Hospitality Market Scraper (Selenium)

### 🎯 Project Overview
A robust **Data Extraction Pipeline** designed to harvest real-time pricing data from Single Page Applications (SPAs) like Booking.com. 

While standard HTTP libraries (`requests`) often fail on modern dynamic websites due to client-side rendering, this project utilizes **Selenium WebDriver** to automate a real browser instance, ensuring 100% data capture of dynamically loaded elements like pricing and availability.

### 💼 Business Use Case
* **Competitive Intelligence:** Monitoring competitor pricing strategies in real-time.
* **Market Positioning:** Analyzing the correlation between "User Ratings" and "Nightly Rates" to identify undervalued properties.
* **Gap Analysis:** Detecting high-demand locations (e.g., New Delhi) with low supply of budget-friendly inventory.

---

### 🏗️ The Extraction Logic (ETL)

**1. EXTRACT (Dynamic Browser Automation):**
* **Tool:** Selenium WebDriver (Chrome)
* **Challenge:** The target site uses "Lazy Loading" (JavaScript), meaning data isn't present in the initial HTML.
* **Solution:** Implemented a browser automation engine that:
    * Launches a controlled Chrome instance with `disable-blink-features` to bypass bot detection.
    * Executes the site's JavaScript to fully render the DOM.
    * Waits for specific DOM elements (`property-card`) to load before extraction.

**2. TRANSFORM (Data Structuring):**
* **Robust Selectors:** Utilized `data-testid` attributes (e.g., `[data-testid="price-and-discounted-price"]`) instead of fragile CSS classes. This ensures the pipeline remains stable even during UI updates.
* **Data Cleaning:**
    * **Sanitization:** Removed currency symbols (`₹`) and formatting commas to convert prices into pure integers.
    * **Error Handling:** Implemented `try-except` blocks for every data field (Price, Rating, Location) to handle missing values (`NA`) gracefully without crashing the pipeline.

**3. LOAD (Storage):**
* Data is structured and exported to a CSV file (`selenium_booking_data.csv`), ready for immediate ingestion into **Power BI**, **Tableau**, or **Python Pandas**.

**4.Reporting & Visualization:**
* Built an interactive Executive Dashboard using Pivot Tables and Slicers.
* Implemented Slicers to allow stakeholders to filter market data by Location and Price Range dynamically.
---

### 🛠️ Technical Stack
* **Language:** Python 3.12
* **Automation Engine:** Selenium WebDriver
* **Browser:** Google Chrome (Headless compliant)
* **Data Format:** CSV (Comma Separated Values)

---

### ⚙️ Installation & Usage

**1. Prerequisites**
* Python 3.x
* Google Chrome installed
* ChromeDriver (handled automatically by Selenium 4.x)

**2. Install Dependencies**
pip install selenium


### ⚠️ Important: Web Scraping Limitations
Please note that this project extracts data from a live, dynamic website (`Booking.com`). The pipeline is subject to the following real-world constraints:

1.  **Frontend Volatility:** The target website frequently updates its DOM structure (A/B testing). While this project uses robust `data-testid` selectors, major UI overhauls may require maintenance updates to the extraction logic.
2.  **Anti-Bot Mechanisms:** High-frequency requests may trigger IP blocking or CAPTCHA challenges. This script implements **Rate Limiting** (randomized 2-5s delays) and **User-Agent Rotation** to mitigate detection, but complete immunity is not guaranteed without enterprise-grade proxy rotation.

### 🔧 Troubleshooting
* **"Found 0 Hotels":** This usually indicates a soft-block or a "CAPTCHA" challenge.
    * *Fix:* Run the script in non-headless mode (default) and manually solve the CAPTCHA if it appears.
* **"Element Not Found":** The site layout may have changed.
    * *Fix:* Open the browser `Inspect` tool and verify if `data-testid="property-card"` still exists.


**Some Related Screenshots**
<img width="1920" height="1080" alt="Screenshot (151)" src="https://github.com/user-attachments/assets/ae69fc4d-8845-4057-b866-dd5479321199" />
<img width="1920" height="1080" alt="Screenshot (150)" src="https://github.com/user-attachments/assets/3706d2aa-f58d-41ed-aba1-57cd7d987c80" />
<img width="1920" height="1080" alt="Screenshot (153)" src="https://github.com/user-attachments/assets/c43c7faa-221c-4a5a-b89b-6affaa869907" />
<img width="1920" height="1080" alt="Screenshot (149)" src="https://github.com/user-attachments/assets/7d5f7428-b058-4bc6-a10a-99007fb9bb31" />
<img width="1920" height="1080" alt="Screenshot (146)" src="https://github.com/user-attachments/assets/b6e49561-196e-4703-a21e-b3ec003a65d0" />



