from selenium import webdriver
import time

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.skillrack.com/faces/ui/profile.xhtml")
driver.maximize_window() 

username = driver.find_element_by_id("input_j_id_u")
username.clear()
username.send_keys("your login id")

password = driver.find_element_by_name("j_password")
password.clear()
password.send_keys("your password")
driver.find_element_by_name("j_id_y").click()




