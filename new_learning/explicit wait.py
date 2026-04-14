from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome()

driver.get("https://www.google.com/")
search_text=WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.NAME,'q'))

)

search_text.send_keys("implicit wait")
driver.save_screenshot("result.png")
search_text.submit()


