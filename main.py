#!/usr/bin/env python3
import time
import winsound
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://terminvereinbarung.leipzig.de/m/leipzig-kfz/extern/calendar/?uid=c97bb32a-92b8-41ba-b5c2-f91d0e90019f"
CHECK_INTERVAL = 300  # 5 minutes

# Edit this to select the desired service (exact match)
SERVICE_NAME = "Umschreibung eines Fahrzeuges mit auswärtigem Kennzeichen"

def get_available_services(driver):
    # Get all available services
    labels = driver.find_elements(By.TAG_NAME, "label")
    services = []

    for label in labels:
        text = label.text.strip()
        if text:
            services.append(text)
    return services

def check_appointments():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(URL)
        time.sleep(3)

        # Find and select service
        labels = driver.find_elements(By.TAG_NAME, "label")
        target_id = None

        for label in labels:
            label_text = label.text.strip()
            if label_text == SERVICE_NAME:
                target_id = label.get_attribute("for")
                if target_id:
                    checkbox = driver.find_element(By.ID, target_id)
                    driver.execute_script("arguments[0].click();", checkbox)
                    time.sleep(0.5)

                    select_elements = driver.find_elements(By.XPATH, f"//select[contains(@id, '{target_id}')]")
                    if select_elements:
                        select = select_elements[0]
                        driver.execute_script("arguments[0].value = '1'; arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", select)
                break

        if not target_id:
            services = get_available_services(driver)
            print(f"Service '{SERVICE_NAME}' not found!")
            print(f"\nAvailable services:")
            for i, service in enumerate(services, 1):
                print(f"{i:2}. {service}")
            print(f"\nUpdate SERVICE_NAME in the script to match the service exactly.")
            return None

        weiter_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='button_next']"))
        )
        driver.execute_script("arguments[0].click();", weiter_button)
        time.sleep(4)

        # Check for "no appointments" banner
        no_appointments = driver.find_elements(By.ID, "error_no_appointment_found")

        if no_appointments:
            return False
        else:
            return True

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        driver.quit()

if __name__ == "__main__":
    print(f"Checking: {SERVICE_NAME}")
    print(f"Interval: {CHECK_INTERVAL // 60} minutes\n")

    try:
        while True:
            result = check_appointments()
            if result is True:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] APPOINTMENTS AVAILABLE!")
                winsound.Beep(1000, 500)
                winsound.Beep(1000, 500)
                winsound.Beep(1000, 500)
            elif result is False:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] No appointments")
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\nStopped")
