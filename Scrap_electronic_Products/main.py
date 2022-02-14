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

df1=pd.read_csv('Product_Details.csv')
df1=pd.concat([df1,pd.DataFrame(columns=['Title','Price','Description','Quantity','Manu_Part_num','Brand'])])
df1=df1.astype(str)

wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='authorization-link']")))
driver.find_element(By.XPATH,"//li[@class='authorization-link']").click()

wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='login[username]']")))
driver.find_element(By.XPATH,"//input[@name='login[username]']").send_keys('sales@auscompcomputers.com')

wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='login[password]']")))
driver.find_element(By.XPATH,"//input[@name='login[password]']").send_keys('Akash1809')

wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Sign In']")))
driver.find_element(By.XPATH,"//span[text()='Sign In']").click()

Prod_Links = df1['Product_URL'].tolist()

i=0
for link in Prod_Links[0:10]:
    driver.get(link)
    try:
        Prod_Title = driver.find_element(By.XPATH,"//span[@class='base']").text
        df1.loc[i,'Title']=Prod_Title
    except:
        df1.loc[i,'Title']=''



    try:
        Price = driver.find_element(By.XPATH,"//span[@class='price']").text
        df1.loc[i,'Price']=Price
    except:
        df1.loc[i,'Price']=''



    try:
        Description = driver.find_element(By.XPATH,"//div[@itemprop='description']").text
        df1.loc[i,'Description']=Description
    except:
        df1.loc[i,'Description']=''



    try:
        Quantity = driver.find_element(By.XPATH,"//div[@class='control stock-availability']").text
        print(Quantity)
        df1.loc[i,'Quantity']=str(Quantity)
    except:
        df1.loc[i,'Quantity']=''


    try:
        driver.find_element(By.XPATH,"//a[@id='tab-label-additional-title']").click()
        Part_Num = driver.find_element(By.XPATH,"//td[@data-th='Manufacturer Part Number']").text
        df1.loc[i,'Manu_Part_num']=Part_Num
    except:
        df1.loc[i,'Manu_Part_num']=''


    try:
        Brand = driver.find_element(By.XPATH,"//td[@data-th='Brand']").text
        df1.loc[i,'Brand']=Brand
    except:
        df1.loc[i,'Brand']=''

    i=i+1

print(df1.head(10))
df1.to_csv('Product_Details.csv')


