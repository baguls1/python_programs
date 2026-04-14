import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_login():

    #launching the browser and open the IDM website
    driver= webdriver.Chrome()
    log_url ='http://192.168.70.201:99/redirect'
    driver.get(log_url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    #select the username and logged in the system
    open_dropdown = driver.find_element(By.ID,'username')

    drop=Select(open_dropdown)
    drop.select_by_value('Nishikant Mokashi')
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
    time.sleep(1)
    title = driver.find_element(By.XPATH,"//h4[normalize-space()='ID Collections']")
    time.sleep(1)


    #To verify that Page title of the application on the dashboard
    if title.text=='ID Collections':
        print("title matched")
    else:
        print('not matched')