from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from List_Products_page import Find_Lst_Products
from List_Products_page_2 import Find_Lst_Products2
from Scrap_details import Prod_Details
from selenium.webdriver import ActionChains

service = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

wait=WebDriverWait(driver, 10)
driver.maximize_window()


#driver.get("https://www.producthunt.com/posts/multiplication-kingdom")

#driver.maximize_window()
#driver.implicitly_wait(20)

#wait=WebDriverWait(driver, 10)

# GetLink = driver.find_element(By.XPATH,"//button[@data-test='get-it-button']")
# act = ActionChains(driver)
# act.move_to_element(GetLink).perform()
# wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_allLinks__2sH2S']//a[1]")))
# Website=driver.find_element(By.XPATH,"//div[@class='styles_allLinks__2sH2S']//a[1]")
# print("Link to website",Website.get_attribute('href'))
#driver.find_element(By.XPATH,"//span[text()='get it']").click()
#driver.switch_to.window(driver.window_handles[-1])
#print(driver.current_url)
#driver.switch_to.window(driver.window_handles[-2])
#print(driver.current_url)

driver.get('https://www.producthunt.com/posts/workdo-2')
wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(@class,'headerPostName')]//a[contains(@href,'/r/')]")))
Prod_name=driver.find_element(By.XPATH,"//h1[contains(@class,'headerPostName')]//a[contains(@href,'/r/')]")
print("Product Name ",Prod_name)

wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='styles_bigButtonCount__1DS7y']")))
Total_Votes=driver.find_element(By.XPATH,"//span[@class='styles_bigButtonCount__1DS7y']")
print("Total Votes ",Total_Votes)

try:
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='get it']/parent::a")))
    Website=driver.find_element(By.XPATH,"//*[text()='get it']/parent::a")
except:
    print("Link not present")
#wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='styles_link__2efWB']")))
#Website=driver.find_element(By.XPATH,"//a[@class='styles_link__2efWB']")


try:
    Count_Reviews = driver.find_element(By.XPATH,"//span[contains(@class,'styles_reviewCountActive')]")
    print("Total Review Count ",Count_Reviews)
except:
    print("No Review Count yet")


try:        
    Review_Score = driver.find_element(By.XPATH,"//span[contains(@class,'styles_rating')]")
    print("Total Review Score ",Review_Score)
except:
    print("No Scores yet")



wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_makersContainer__1N77x'][1]//div[@class='styles_content__2OcVn']//div")))
lst_Hunters = driver.find_elements(By.XPATH,"//div[@class='styles_makersContainer__1N77x'][1]//div[@class='styles_content__2OcVn']//div")
Hunters=[]
for item in lst_Hunters:
    Hunters.append(item.text)
print("List of Hunters ",Hunters)



wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_makersContainer__1N77x'][2]//div[@class='styles_content__2OcVn']//div")))
lst_Founders = driver.find_elements(By.XPATH,"//div[@class='styles_makersContainer__1N77x'][2]//div[@class='styles_content__2OcVn']//div")
Founders=[]
for item in lst_Founders:
    Founders.append(item.text)
print("list of Founders ",Founders)


    
lst_Industry_type=[]
elemnt1=driver.find_element(By.XPATH,"//div[@class='styles_topicPriceWrap__2fqZ7']//a[contains(@href,'/topics')]")
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_topicPriceWrap__2fqZ7']//div/a[@title='More options']")))
driver.find_element(By.XPATH,"//div[@class='styles_topicPriceWrap__2fqZ7']//div/a[@title='More options']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='styles_option__b7Uwf']//a[contains(@href,'/topics')]")))
Others = driver.find_elements(By.XPATH,"//li[@class='styles_option__b7Uwf']//a[contains(@href,'/topics')]")
lst_Industry_type.extend(Others)

lst_Industry_type.append(elemnt1)
Industry_type=[]
for item in lst_Industry_type:
    Industry_type.append(item.text)

print("List of Industry Type ",Industry_type)


