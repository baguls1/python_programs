from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
search_text=driver.find_element(By.NAME,"q")
search_text.send_keys("implicit wait")
search_text.submit()
