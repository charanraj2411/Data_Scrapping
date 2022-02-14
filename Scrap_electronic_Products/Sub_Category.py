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

df1=pd.read_csv('Sub-Category.csv')
print(df1)

wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='authorization-link']")))
driver.find_element(By.XPATH,"//li[@class='authorization-link']").click()

wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='login[username]']")))
driver.find_element(By.XPATH,"//input[@name='login[username]']").send_keys('sales@auscompcomputers.com')

wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='login[password]']")))
driver.find_element(By.XPATH,"//input[@name='login[password]']").send_keys('Akash1809')

wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Sign In']")))
driver.find_element(By.XPATH,"//span[text()='Sign In']").click()


Cat_Links = df1['Link'].tolist()



print(len(Cat_Links))


lst_products_links=[]
for item in Cat_Links:
    driver.get(item)
    Page_end = driver.find_element(By.XPATH,"//a[text()='About Us']")
    driver.execute_script("arguments[0].scrollIntoView();", Page_end)
    try:
        prod_lst = driver.find_elements(By.XPATH,"//a[@class='product-item-link']")
        print(len(prod_lst))
        for item in prod_lst:
            lst_products_links.append(item.get_attribute('href'))
    except:
        continue

print(len(lst_products_links))

df2=pd.DataFrame(lst_products_links,columns=['Product_URL'])
df2.to_csv('Product_Details.csv')




