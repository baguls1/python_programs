import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID,"username").send_keys("tomsmith")
driver.find_element(By.NAME,"password").send_keys("SuperSecretPassword!")
driver.find_element(By.XPATH,"//button[@type='submit']")
time.sleep((2))
print("logged in successfully!!!")
driver.close()