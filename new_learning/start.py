# chrome is the class
# driver is object so that all the class object access its properties
# driver = webdriver.Chrome( call method for opening a chrome browser)


from selenium import webdriver
import time

from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get( "https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@placeholder='Search for Vegetables and Fruits']").send_keys('Tomato')
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
driver.close()


