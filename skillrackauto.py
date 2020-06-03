from selenium import webdriver
import time

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.skillrack.com/faces/ui/profile.xhtml")
driver.maximize_window() 

username = driver.find_element_by_id("input_j_id_u")
username.clear()
username.send_keys("111717104070@rmkec")

password = driver.find_element_by_name("j_password")
password.clear()
password.send_keys("7861")
driver.find_element_by_name("j_id_y").click()
driver.get("https://www.skillrack.com/faces/ui/profile.xhtml")
time.sleep(5)
#driver.find_element(By.className("right floated")).click()
driver.find_element_by_class_name("item").click()
time.sleep(2)
driver.find_element_by_name("examtbl:0:j_id_54").click()
#driver.find_element_by_name("j_id_9:j_id_3n").click()
time.sleep(2)
driver.find_element_by_id("j_id_4p:j_id_5j").click()
time.sleep(2)

driver.find_element_by_name("j_id_4p:j_id_5p").click()




