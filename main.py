# AUTO-FILL Google Form (robust)
# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random

# ================= CONFIG =================
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScLCUqWXT9h4Hx7pFObYKZX8rhabfFvoNNqYUuwxVnuOEo--Q/viewform?usp=send_form"
NUM_SUBMISSIONS = 10   # set to 100 when ready
# ==========================================

def start_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")    # uncomment if you want headless (not recommended while debugging)
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    return driver

def click_by_text(driver, text, timeout=8):
    """
    Try several XPaths to find an element by visible text and click it.
    Returns True on success, False if not found.
    """
    xpaths = [
        # radio / checkbox controls that contain the label text
        f"//div[@role='radio' and .//div[contains(normalize-space(.), \"{text}\")]]",
        f"//div[@role='checkbox' and .//div[contains(normalize-space(.), \"{text}\")]]",
        # generic span/div/label matches
        f"//span[normalize-space()=\"{text}\"]",
        f"//div[normalize-space()=\"{text}\"]",
        f"//*[normalize-space()=\"{text}\"]",
        f"//*[contains(normalize-space(.), \"{text}\")]"
    ]
    for xp in xpaths:
        try:
            el = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xp)))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            el.click()
            return True
        except Exception:
            continue
    print(f"[WARN] Could not find/click option with text: {text!r}")
    return False

def submit_form(driver):
    # Submit button is localized in your form as '送信' — try several fallbacks
    submit_text_candidates = ("送信", "Submit", "Submit form", "送信する")
    for txt in submit_text_candidates:
        try:
            span = driver.find_element(By.XPATH, f"//span[normalize-space()='{txt}']")
            btn = span.find_element(By.XPATH, "./ancestor::button")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            btn.click()
            return True
        except Exception:
            pass
    # fallback: try any clickable button
    try:
        btn = driver.find_element(By.XPATH, "//button[@type='button' or @role='button']")
        btn.click()
        return True
    except Exception:
        print("[ERROR] Submit button not found.")
        return False

# --- prepare some varied responses that match the exact labels on your form ---
sample_responses = [
    {
        "age": "18-24",
        "search_method": "Airline websites",
        "challenges": ["Prices change too quickly", "Hard to compare across airlines"],
        "need_system": "Yes",
        "difficulty": "2",
        "priority": "Ticket price"
    },
    {
        "age": "25-34",
        "search_method": "Mobile apps/websites (e.g., Skyscanner, Traveloka, Kayak)",
        "challenges": ["Searching takes too much time", "Hidden fees or unclear pricing"],
        "need_system": "Maybe",
        "difficulty": "3",
        "priority": "Flight schedule/timing"
    },
    {
        "age": "35-44",
        "search_method": "Travel agencies",
        "challenges": ["Limited access to platforms"],
        "need_system": "Yes",
        "difficulty": "3",
        "priority": "Airline reputation"
    }
]

def run():
    driver = start_driver()
    try:
        for i in range(NUM_SUBMISSIONS):
            resp = random.choice(sample_responses)
            driver.get(FORM_URL)
            time.sleep(2)  # let JS render the form

            # Click options (must match the form visible text exactly)
            click_by_text(driver, resp["age"])
            click_by_text(driver, resp["search_method"])
            # checkboxes: click each challenge
            for ch in resp["challenges"]:
                click_by_text(driver, ch)
                time.sleep(0.2)
            click_by_text(driver, resp["need_system"])
            click_by_text(driver, resp["difficulty"])
            click_by_text(driver, resp["priority"])

            time.sleep(0.6)
            if not submit_form(driver):
                print("Failed to submit. Stopping.")
                break

            # small wait, then attempt to click "Submit another response" if it appears
            time.sleep(2)
            try:
                # There may be a link/button to submit another response — language varies
                again = driver.find_element(By.XPATH, "//a[contains(., 'Submit another response') or contains(., 'フォームをクリア') or contains(., 'Another response')]")
                again.click()
                time.sleep(1)
            except Exception:
                # if not present, simply continue to next iteration; the script will reload the form anyway
                pass

            sleep_time = random.uniform(1.0, 2.5)
            time.sleep(sleep_time)
            print(f"Submitted #{i+1}")
    finally:
        driver.quit()
        print("Done.")

if __name__ == "__main__":
    run()
