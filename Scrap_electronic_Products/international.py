import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome("C:/Users/DELL/Downloads/chromedriver.exe")

driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://www.com1.com.au/')
wait=WebDriverWait(driver, 2)

wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='authorization-link']")))
driver.find_element(By.XPATH,"//li[@class='authorization-link']").click()

wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='login[username]']")))
driver.find_element(By.XPATH,"//input[@name='login[username]']").send_keys('sales@auscompcomputers.com')

wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='login[password]']")))
driver.find_element(By.XPATH,"//input[@name='login[password]']").send_keys('Akash1809')

wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Sign In']")))
driver.find_element(By.XPATH,"//span[text()='Sign In']").click()

driver.get('https://www.com1.com.au/msi-27-fhd-19201080-60hz-ips-flat-screen-hdmi-vga-vesa-speakers-pro-mp271.html')

Prod_Title = driver.find_element(By.XPATH,"//span[@class='base']").text
print('Product title is ',Prod_Title)

Price = driver.find_element(By.XPATH,"//span[@class='price']").text
print('Product Price is ',Price)

Description = driver.find_element(By.XPATH,"//div[@itemprop='description']").text
print('Product description ',Description)

Quantity = driver.find_element(By.XPATH,"//div[@class='control stock-availability']").text
print('Product Quantity', Quantity)


Part_num = driver.find_element(By.XPATH,"//div[@itemprop='sku']").text
print('Product Manufacturer part num  is ', Part_num)

### click on Details tab
driver.find_element(By.XPATH,"//a[@id='tab-label-description-title']").click()


Model_Name = driver.find_element(By.XPATH,"//table/tbody/tr[3]/td[2]").text
print('Model Name', Model_Name)

Spec_item_1 = driver.find_element(By.XPATH,"//table/tbody/tr[5]/td[1]").text
Spec_item_1_val = driver.find_element(By.XPATH,"//table/tbody/tr[5]/td[2]").text
print(''+'is given as '+'', Spec_item_1,Spec_item_1_val)

