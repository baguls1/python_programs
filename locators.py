import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://demo.automationtesting.in/Register.html')
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys('saurabh')
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys('bagul')
driver.find_element(By.XPATH,"//input[@type='email']").send_keys('bagulsaur@gmail.com')
driver.find_element(By.XPATH,"//input[@type='tel']").send_keys('9875625489')
driver.find_element(By.XPATH,"//input[@name='radiooptions']").click()
driver.find_element(By.XPATH,"//select[@id='countries']").click()
driver.find_element(By.XPATH,"//button[@id='submitbtn']").click()


time.sleep(2)