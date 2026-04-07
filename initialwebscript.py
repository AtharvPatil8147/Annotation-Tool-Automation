import csv
import time
import random
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nextgenvectora.com/DAT/user/create-annotation")

    input("Login manually, then press ENTER...")

    with open("data.csv", newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)

        print("Detected columns:", reader.fieldnames)  # DEBUG

        

        for row in reader:
            try:
                # 🔽 Select Annotation Type (Sentence = value 2)
                page.select_option("#annotation_type_id", value="2")

                # 🔽 Select Language (Marathi = value 3)
                page.select_option("#language_id", value="3")

                # ⏳ WAIT for dialects to load
                time.sleep(2)

                # 🔽 Select Source Dialect
                page.select_option("#source_dialect_id", index=1)

                # 🔽 Select Destination Dialect
                page.select_option("#destination_dialect_id", index=6)

                print(row)  # DEBUG

                page.fill("#source_text", row["Source"])
                page.fill("#annotated_text", row["Annotated"])
                page.fill("#english_equivalent", row["English"])

                # 🔽 Fill Text Fields
                page.fill("#source_text", row["Source"])
                page.fill("#annotated_text", row["Annotated"])
                page.fill("#english_equivalent", row["English"])

                # 🔽 Submit
                page.click('button[type="submit"]')

                print("✅ Submitted:", row["Source"])

                # ⏳ Random delay (anti-detection)
                time.sleep(random.uniform(2, 9))

            except Exception as e:
                print("❌ Error:", e)
                continue

    browser.close()
