import csv
import time
import random
from playwright.sync_api import sync_playwright

from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

#  READ LOGIN CREDENTIALS
#with open("login.csv", newline='', encoding='utf-8-sig') as login_file:
#    login_reader = csv.DictReader(login_file)
#    login_data = next(login_reader)  # first row

#EMAIL = login_data["email"]
#PASSWORD = login_data["password"]
line_count = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    #  STEP 1: LOGIN PAGE
    page.goto("https://nextgenvectora.com/DAT/index")

    page.fill("#email", EMAIL)
    page.fill("#password", PASSWORD)
    page.click('button[type="submit"]')

    #  Wait for dashboard to load
    page.wait_for_load_state("networkidle")
    print(" Logged in")

    #  STEP 2: CLICK "CREATE NEW ANNOTATION"
    page.wait_for_selector('a[href="/DAT/user/create-annotation.php"]')
    page.click('a[href="/DAT/user/create-annotation.php"]')

    print(" Navigated to annotation page")

    #  Wait for form to load
    page.wait_for_selector("#source_text")

    #  STEP 3: CSV LOOP
    with open("data.csv", newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)

        print("Detected columns:", reader.fieldnames)

        for row in reader:
            try:
                #  Select Annotation Type (Paragraph = value 3)
                page.select_option("#annotation_type_id", value="1")

                #  Select Language (Marathi = value 3)
                page.select_option("#language_id", value="3")

                #  WAIT for dialects to load
                time.sleep(1)

                #  Select Source Dialect
                page.select_option("#source_dialect_id", index=1)

                #  Select Destination Dialect
                page.select_option("#destination_dialect_id", index=6)

                print(row)
                line_count = line_count+1
                print("Line number: ", line_count, "done!")

                #  Fill Text Fields
                page.fill("#source_text", row["Source"])
                page.fill("#annotated_text", row["Annotated"])
                page.fill("#english_equivalent", row["English"])

                #  Submit
                page.click('button[type="submit"]')

                print(" Submitted:", row["Source"])

                #  Wait for form to reload again
                page.wait_for_selector("#source_text")

                #  Random delay (anti-detection)
                time.sleep(random.uniform(1, 2))

            except Exception as e:
                print(" Error:", e)
                continue

    browser.close()
