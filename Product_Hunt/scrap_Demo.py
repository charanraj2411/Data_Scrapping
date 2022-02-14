from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.producthunt.com/")
print("The title is ",driver.title)


driver.find_element(By.XPATH,"//a[contains(@data-test,'tagline')]").click()


Prod_name=driver.find_element(By.XPATH,"//h1[contains(@class,'headerPostName')]//a[contains(@href,'/r/')]")
print("Product Name ",Prod_name.text)


element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//h1[contains(@class,'headerPostName')]//a")))


Total_Votes=driver.find_element(By.XPATH,"//span[@class='styles_bigButtonCount__1DS7y']")
print("Total votes",Total_Votes.text)


Website=driver.find_element(By.XPATH,"//*[text()='get it']/parent::a")
print("Link to website",Website.get_attribute('href'))


Count_Reviews = driver.find_element(By.XPATH,"//span[contains(@class,'styles_reviewCountActive')]")
print("Total Reviews",Count_Reviews.text)


Review_Score = driver.find_element(By.XPATH,"//span[contains(@class,'styles_rating')]")
print("Total Review Score",Review_Score.text)


lst_Hunters = driver.find_elements(By.XPATH,"//div[@class='styles_makersContainer__1N77x'][1]//div[@class='styles_content__2OcVn']//div")
print("Below is the list of Hunters")
for item in lst_Hunters:
    print(item.text)


lst_Founders = driver.find_elements(By.XPATH,"//div[@class='styles_makersContainer__1N77x'][2]//div[@class='styles_content__2OcVn']//div")
print("Below is the list of Founders")
for item in lst_Founders:
    print(item.text)


elemnt1=driver.find_element(By.XPATH,"//div[@class='styles_topicPriceWrap__2fqZ7']//a[contains(@href,'/topics')]")


driver.find_element(By.XPATH,"//div[@class='styles_topicPriceWrap__2fqZ7']//div/a[@title='More options']").click()


element = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.XPATH, "//div[@class='styles_topicPriceWrap__2fqZ7']//div/a[@title='More options']")))


Industry_type = driver.find_elements(By.XPATH,"//li[@class='styles_option__b7Uwf']//a[contains(@href,'/topics')]")
Industry_type.append(elemnt1)


print("Below is the list of Industry_type")
for item in Industry_type:
       print(item.text)


driver.find_element(By.XPATH,"//a[@data-test='modal-close']").click()