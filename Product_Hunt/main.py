from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from List_Products_page import Find_Lst_Products
from List_Products_page_2 import Find_Lst_Products2
from Scrap_details import Prod_Details

## Create an instance of Chrome Driver
service = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

wait=WebDriverWait(driver, 10)

## Maximize the window
driver.maximize_window()
driver.implicitly_wait(20)

## Navigate to the website
driver.get("https://www.producthunt.com/")
print("The title is ",driver.title)


view_product = driver.find_element(By.XPATH,"//button[text()='View all products']")
driver.execute_script("arguments[0].scrollIntoView();", view_product)
driver.execute_script("arguments[0].click();", view_product)
show_less = driver.find_element(By.XPATH,"//button[text()='Show less']")
driver.execute_script("arguments[0].scrollIntoView();", show_less)
    #view_product.click()

container = 'homepage-section-0'
lst_products_page = driver.find_elements(By.XPATH,"//div[@data-test='"+container+"']//a[contains(@data-test,'tagline')]")
print(len(lst_products_page))

for item in lst_products_page:
    item.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(@class,'headerPostName')]//a[contains(@href,'/r/')]")))
    Prod_name=driver.find_element(By.XPATH,"//h1[contains(@class,'headerPostName')]//a[contains(@href,'/r/')]")
    print("Product Name ",Prod_name.text)

# container_no=0
# prod_lst=Find_Lst_Products2(driver,container_no)
# Prod_Details(driver,prod_lst)

# container_no=1
# prod_lst=Find_Lst_Products2(driver,container_no)
# Prod_Details(driver,prod_lst)