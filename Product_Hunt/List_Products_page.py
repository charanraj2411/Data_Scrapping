from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def Find_Lst_Products(driver):
    lst_products_page = driver.find_elements(By.XPATH,"//a[contains(@data-test,'tagline')]")
    print(len(lst_products_page))
    return lst_products_page

