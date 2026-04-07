import csv
import time
import random
from playwright.sync_api import sync_playwright

# 🔽 READ LOGIN CREDENTIALS
with open("login.csv", newline='', encoding='utf-8-sig') as login_file:
    login_reader = csv.DictReader(login_file)
    login_data = next(login_reader)  # first row

EMAIL = login_data["email"]
PASSWORD = login_data["password"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 🔽 STEP 1: LOGIN PAGE
    page.goto("https://nextgenvectora.com/DAT/index")

    page.fill("#email", EMAIL)
    page.fill("#password", PASSWORD)
    page.click('button[type="submit"]')

    # 🔽 Wait for dashboard
    page.wait_for_load_state("networkidle")
    print("✅ Logged in")

    # 🔽 STEP 2: GO TO CREATE ANNOTATION PAGE
    page.wait_for_selector('a[href="/DAT/user/create-annotation.php"]')
    page.click('a[href="/DAT/user/create-annotation.php"]')

    print("✅ Navigated to annotation page")

    # 🔽 Wait for form
    page.wait_for_selector("#source_text")

    # 🔽 STEP 3: CSV LOOP
    with open("data.csv", newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)

        print("Detected columns:", reader.fieldnames)

        for row in reader:
            try:
                # Annotation Type → Sentence
                page.select_option("#annotation_type_id", value="2")

                # Language → Marathi
                page.select_option("#language_id", value="3")

                time.sleep(2)

                # Dialects (adjust if needed)
                page.select_option("#source_dialect_id", index=1)
                page.select_option("#destination_dialect_id", index=6)

                # Fill fields
                page.fill("#source_text", row["Source"])
                page.fill("#annotated_text", row["Annotated"])
                page.fill("#english_equivalent", row["English"])

                # Submit
                page.click('button[type="submit"]')

                print("✅ Submitted:", row["Source"])

                # Wait for reload
                page.wait_for_selector("#source_text")

                time.sleep(random.uniform(2, 5))

            except Exception as e:
                print("❌ Error:", e)
                continue

    browser.close()