from selenium import webdriver
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
window=driver.window_handles
driver.switch_to.window(window[1])
print(driver.title)


window=driver.window_handles
driver.switch_to.window(window[1])