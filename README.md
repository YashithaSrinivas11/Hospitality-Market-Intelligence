# 🏨 Dynamic Hospitality Market Scraper (Selenium)

## 🎯 Project Overview

A robust **Data Extraction Pipeline** designed to harvest real-time pricing data from Single Page Applications (SPAs) like Booking.com.

Traditional HTTP libraries (`requests`, `BeautifulSoup`) often fail on modern dynamic websites due to client-side rendering.
This project uses **Selenium WebDriver** to automate a real browser instance, ensuring reliable extraction of dynamically loaded elements such as pricing and availability.

---

## 💼 Business Use Case

* **Competitive Intelligence** — Monitor competitor pricing strategies in real-time
* **Market Positioning** — Identify undervalued properties by correlating ratings vs pricing
* **Demand Gap Analysis** — Detect high-demand locations (e.g., New Delhi) lacking budget inventory

---

## 🏗️ Architecture — ETL Pipeline

### 1️⃣ Extract (Dynamic Browser Automation)

**Tool:** Selenium WebDriver (Chrome)

**Problem:** Target website uses lazy-loading JavaScript → data not present in initial HTML

**Solution Implemented**

* Automated Chrome instance execution
* JavaScript rendering before extraction
* Intelligent wait conditions for `property-card` elements
* Bot-evasion flags (`disable-blink-features`)

---

### 2️⃣ Transform (Data Structuring)

**Stable Selectors**

* Used `data-testid` attributes instead of fragile CSS classes

  * Example: `[data-testid="price-and-discounted-price"]`

**Data Cleaning**

* Removed currency symbols (₹) and commas
* Converted price to integer format
* Handled missing fields using safe exception handling (`NA` fallback)

---

### 3️⃣ Load (Storage)

Exported structured dataset to:

```
selenium_booking_data.csv
```

Ready for:

* Power BI
* Tableau
* Pandas analysis

---

### 4️⃣ Reporting & Visualization

Created an interactive executive dashboard using:

* Pivot Tables
* Slicers (Location & Price Range filtering)

---

## 🛠️ Technical Stack

| Component        | Technology                          |
| ---------------- | ----------------------------------- |
| Language         | Python 3.12                         |
| Automation       | Selenium WebDriver                  |
| Browser          | Google Chrome (Headless Compatible) |
| Containerization | Docker                              |
| Output           | CSV                                 |
| Visualization    | Excel / Power BI                    |

---

# 🐳 Containerized Execution (Docker)

To ensure reproducibility and eliminate environment setup issues, the scraper is fully containerized.

### Build Image

```bash
docker build -t booking-scraper .
```

### Run Scraper

```bash
docker run --rm -v "${PWD}:/app" booking-scraper
```

### What This Does

* Runs the scraper inside an isolated container
* Mounts your current folder to `/app`
* Automatically saves output CSV to your local machine

**Benefit:**
Anyone can run the project without installing Python, Chrome, or dependencies.

---

## ⚙️ Local Installation (Optional — Non Docker)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Script

```bash
python main.py
```

---

## ⚠️ Real-World Scraping Constraints

1. **Frontend Volatility**

   * Websites frequently change DOM structure
   * Stable selectors reduce but don’t eliminate maintenance

2. **Anti-Bot Protection**

   * CAPTCHA / IP blocking possible
   * Implemented:

     * Random delays (2–5 sec)
     * User-agent rotation
     * Non-headless fallback

---

## 🔧 Troubleshooting

**Found 0 Hotels**

> Soft block or CAPTCHA triggered
> Fix: Run in non-headless mode and solve CAPTCHA manually

**Element Not Found**

> DOM structure changed
> Fix: Verify selector using browser inspect tool

---

## 📊 Sample Outputs

<img width="1920" height="1080" alt="Screenshot (151)" src="https://github.com/user-attachments/assets/ae69fc4d-8845-4057-b866-dd5479321199" />
<img width="1920" height="1080" alt="Screenshot (150)" src="https://github.com/user-attachments/assets/3706d2aa-f58d-41ed-aba1-57cd7d987c80" />
<img width="1920" height="1080" alt="Screenshot (153)" src="https://github.com/user-attachments/assets/c43c7faa-221c-4a5a-b89b-6affaa869907" />
<img width="1920" height="1080" alt="Screenshot (149)" src="https://github.com/user-attachments/assets/7d5f7428-b058-4bc6-a10a-99007fb9bb31" />
<img width="1920" height="1080" alt="Screenshot (146)" src="https://github.com/user-attachments/assets/b6e49561-196e-4703-a21e-b3ec003a65d0" />

---

## 🚀 Key Engineering Takeaways

* Handling dynamic DOM rendering in modern SPAs
* Designing resilient scraping pipelines
* Anti-bot mitigation strategies
* Data cleaning for analytics pipelines
* Reproducible deployments via Docker

---




