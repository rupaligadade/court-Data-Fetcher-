from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_case_data(case_type, case_number, filing_year):
    # ✅ New correct way with Service() wrapper
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.google.com")
        time.sleep(2)

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(f"{case_type} {case_number} {filing_year}")
        time.sleep(2)

        return {
            "parties": f"{case_type}-{case_number}-{filing_year} vs Respondent",
            "filing_date": "2024-06-15",
            "next_hearing": "2025-08-20",
            "pdf_link": "https://example.com/sample-order.pdf"
        }

    except Exception as e:
        return {"error": str(e)}
    finally:
        driver.quit()