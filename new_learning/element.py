from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/python/how-to-handle-alert-prompts-in-selenium-python/")
text= driver.find_element(By.XPATH,"//h1[normalize-space()='How to handle alert prompts in Selenium Python ?']").text

print(text)
driver.close()