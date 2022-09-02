import time
# import outlook
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://192.168.79.225:8112/")
elemento1 = driver.find_element(By.ID, 'user')
elemento1.clear()
elemento1.send_keys("root")
elemento2 = driver.find_element(By.NAME, 'pass')
elemento2.clear()
elemento2.send_keys("password")
driver.find_element(By.CLASS_NAME, "button").click()
time.sleep(2)
driver.get('http://192.168.79.225:8112')

elemento3 = driver.find_element(By.NAME,"Subject")
elemento3.clear()
elemento3.send_keys("PRUEBA-DEVOPS-MATIAS-GARCIA")

time.sleep(2)
elemento4 = driver.find_element(By.CLASS_NAME,"button").click()
time.sleep(5)

driver.close()