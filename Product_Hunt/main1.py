from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from List_Products_page import Find_Lst_Products
from List_Products_page_2 import Find_Lst_Products2
from Scrap_details import Prod_Details
import pandas as pd


column_names = ["Product_Name", "Total_votes", "Website_Link","Total_Reviews","Review_Score","Hunters","Founders","Industry_Type"]
df = pd.DataFrame(columns = column_names)


## Create an instance of Chrome Driver
service = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

wait=WebDriverWait(driver, 10)

## Maximize the window
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.producthunt.com/")

lst_products_links=[]

for section in range(0,10):
    container = 'homepage-section-'+str(section)
    view_product = driver.find_element(By.XPATH,"//div[@data-test='"+container+"']//button[text()='View all products']")
    driver.execute_script("arguments[0].scrollIntoView();", view_product)
    driver.execute_script("arguments[0].click();", view_product)
    show_less = driver.find_element(By.XPATH,"//div[@data-test='"+container+"']//button[text()='Show less']")
    driver.execute_script("arguments[0].scrollIntoView();", show_less)
    lst_products_page = driver.find_elements(By.XPATH,"//div[@data-test='"+container+"']//a[contains(@data-test,'tagline')]")
    print(len(lst_products_page))
    for item in lst_products_page:
        lst_products_links.append(item.get_attribute('href'))
print(len(lst_products_links))


i=0
link1=lst_products_links[0:313]
for item in link1:
    driver.get(item)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(@class,'headerPostName')]//a[contains(@href,'/r/')]")))
    Prod_name=driver.find_element(By.XPATH,"//h1[contains(@class,'headerPostName')]//a[contains(@href,'/r/')]")
    df.loc[i,"Product_Name"]=Prod_name.text
    print("Product Name ",Prod_name.text)



    wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='styles_bigButtonCount__1DS7y']")))
    Total_Votes=driver.find_element(By.XPATH,"//span[@class='styles_bigButtonCount__1DS7y']")
    df.loc[i,"Total_votes"]=Total_Votes.text



    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='get it']/parent::a")))
        Website=driver.find_element(By.XPATH,"//*[text()='get it']/parent::a")
        df.loc[i,"Website_Link"]=Website.get_attribute('href')
    except :
        #print("Link not present")
        df.loc[i,"Website_Link"]="Link not present"


    try:
        Count_Reviews = driver.find_element(By.XPATH,"//span[contains(@class,'styles_reviewCountActive')]")
        df.loc[i,"Total_Reviews"]=Count_Reviews.text
    except :
        #print("Total Reviews : No reviews until now")
        df.loc[i,"Total_Reviews"]="No reviews until now"
    


    try:
        Review_Score = driver.find_element(By.XPATH,"//span[contains(@class,'styles_rating')]")
        df.loc[i,"Review_Score"]=Review_Score.text
    except :
        df.loc[i,"Review_Score"]="No Review Score until now"


    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_makersContainer__1N77x'][1]//div[@class='styles_content__2OcVn']//div")))
        lst_Hunters = driver.find_elements(By.XPATH,"//div[@class='styles_makersContainer__1N77x'][1]//div[@class='styles_content__2OcVn']//div")
        Hunters=[]
        for item in lst_Hunters:
            Hunters.append(item.text)
        df.at[i,'Hunters']=Hunters
    except:
        df.at[i,'Hunters']="Hunter Not found"



    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_makersContainer__1N77x'][2]//div[@class='styles_content__2OcVn']//div")))
        lst_Founders = driver.find_elements(By.XPATH,"//div[@class='styles_makersContainer__1N77x'][2]//div[@class='styles_content__2OcVn']//div")
        Founders=[]
        for item in lst_Founders:
            Founders.append(item.text)
        df.loc[i,"Founders"]=Founders            
    except:
        df.loc[i,"Founders"]="No Founders exist yet"  


    
    lst_Industry_type=[]
    elemnt1=driver.find_element(By.XPATH,"//div[@class='styles_topicPriceWrap__2fqZ7']//a[contains(@href,'/topics')]")
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_topicPriceWrap__2fqZ7']//div/a[@title='More options']")))
        driver.find_element(By.XPATH,"//div[@class='styles_topicPriceWrap__2fqZ7']//div/a[@title='More options']").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='styles_option__b7Uwf']//a[contains(@href,'/topics')]")))
        Others = driver.find_elements(By.XPATH,"//li[@class='styles_option__b7Uwf']//a[contains(@href,'/topics')]")
        lst_Industry_type.extend(Others)
    except:
        pass



    lst_Industry_type.append(elemnt1)
    Industry_type=[]
    for item in lst_Industry_type:
        Industry_type.append(item.text)
    df.loc[i,"Industry_Type"]=Industry_type
    i=i+1
#print(df)


print(df.loc[:,'Product_Name'])
print(df.loc[:,'Total_votes'])
print(df.loc[:,'Website_Link'])
print(df.loc[:,'Total_Reviews'])
print(df.loc[:,'Review_Score'])
print(df.loc[:,'Hunters'])
print(df.loc[:,'Founders'])
print(df.loc[:,'Industry_Type'])