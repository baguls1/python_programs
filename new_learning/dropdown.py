

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
value=driver.find_element(By.ID,"dropdown")
drop_down=Select(value)
drop_down.select_by_visible_text("Option 1")
driver.save_screenshot("dropdown.png")



