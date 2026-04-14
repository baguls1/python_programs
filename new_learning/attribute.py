

from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

# Search for something

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Python Selenium tutorial")

search_box.submit()

time.sleep(2)

# Extract all result titles

results = driver.find_elements(By.XPATH, "//h3")

for idx, result in enumerate(results):
    print(f"{idx + 1}. {result.text}")

driver.quit()