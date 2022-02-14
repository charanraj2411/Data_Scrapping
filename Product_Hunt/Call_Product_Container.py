from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

## Maximize the window
driver.maximize_window()
driver.implicitly_wait(20)

## Navigate to the website
driver.get("https://www.producthunt.com/")

for containers in range(1):
    container = 'homepage-section-'+str(containers)
    #print(container)
    driver.find_element(By.XPATH,"//div[@data-test='"+container+"']//button[text()='View all products']").click()
    time.sleep(10)
    lst_products_page = driver.find_elements(By.XPATH,"div[@data-test='"+container+"']//a[contains(@data-test,'tagline')]")
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@data-test='"+container+"']//a[contains(@data-test,'tagline')]")))
    
    print(len(lst_products_page))

    