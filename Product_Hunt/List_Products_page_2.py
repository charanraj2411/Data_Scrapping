from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def Find_Lst_Products2(driver,container_no):
    wait=WebDriverWait(driver, 10)
    container = 'homepage-section-'+str(container_no)

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-test='"+container+"']//button[text()='View all products']"))).click()

    lst_products_page = driver.find_elements(By.XPATH,"//div[@data-test='"+container+"']//a[contains(@data-test,'tagline')]")

    print(len(lst_products_page))
    return lst_products_page

