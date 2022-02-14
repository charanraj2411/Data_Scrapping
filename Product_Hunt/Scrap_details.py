from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

def Prod_Details(driver,prod_lst):
    wait=WebDriverWait(driver, 10)
    for prod  in prod_lst:
        prod.click()
        time.sleep(30)


        ## Find Product Name
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(@class,'headerPostName')]//a[contains(@href,'/r/')]")))
        Prod_name=driver.find_element(By.XPATH,"//h1[contains(@class,'headerPostName')]//a[contains(@href,'/r/')]")
        print("Product Name ",Prod_name.text)



        ## Total Votes
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='styles_bigButtonCount__1DS7y']")))
        Total_Votes=driver.find_element(By.XPATH,"//span[@class='styles_bigButtonCount__1DS7y']")
        print("Total votes",Total_Votes.text)



        ## Find Link to Website
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='get it']/parent::a")))
            Website=driver.find_element(By.XPATH,"//*[text()='get it']/parent::a")
            print("Link to website",Website.get_attribute('href'))
        except :
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='styles_link__2efWB']")))
                Website=driver.find_element(By.XPATH,"//a[@class='styles_link__2efWB']")           
                print("Link to website",Website.get_attribute('href'))
            except :
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='get it']"))).click()
                    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_allLinks__2sH2S']//a[1]")))
                    Website=driver.find_element(By.XPATH,"//div[@class='styles_allLinks__2sH2S']//a[1]")
                    print("Link to website",Website.get_attribute('href'))
                except:
                    try:
                        driver.find_element(By.XPATH,"//span[text()='get it']").click()
                        driver.switch_to.window(driver.window_handles[-1])
                        print("Link to website",driver.current_url)
                        driver.switch_to.window(driver.window_handles[-2])
                    except:
                        print("Link not found")



        ## Count the Reviews
        try:
            Count_Reviews = driver.find_element(By.XPATH,"//span[contains(@class,'styles_reviewCountActive')]")
            print("Total Reviews: ",Count_Reviews.text)
        except :
            print("Total Reviews : No reviews until now")



        ## Find Review Score
        try:
            Review_Score = driver.find_element(By.XPATH,"//span[contains(@class,'styles_rating')]")
            print("Total Review Score",Review_Score.text)
        except :
            print("Total Review Score : No Score until now")



        ## Find list of hunters
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_makersContainer__1N77x'][1]//div[@class='styles_content__2OcVn']//div")))
        lst_Hunters = driver.find_elements(By.XPATH,"//div[@class='styles_makersContainer__1N77x'][1]//div[@class='styles_content__2OcVn']//div")
        print("Below is the list of Hunters")
        for item in lst_Hunters:
            print(item.text)



        ## Find list of Founders
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_makersContainer__1N77x'][2]//div[@class='styles_content__2OcVn']//div")))
            lst_Founders = driver.find_elements(By.XPATH,"//div[@class='styles_makersContainer__1N77x'][2]//div[@class='styles_content__2OcVn']//div")
            print("Below is the list of Founders")
            for item in lst_Founders:
                print(item.text)   
        except:
            print("No Founders yet")



        ## Find the Industry Type
        Industry_type=[]
        elemnt1=driver.find_element(By.XPATH,"//div[@class='styles_topicPriceWrap__2fqZ7']//a[contains(@href,'/topics')]")
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='styles_topicPriceWrap__2fqZ7']//div/a[@title='More options']")))
            driver.find_element(By.XPATH,"//div[@class='styles_topicPriceWrap__2fqZ7']//div/a[@title='More options']").click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='styles_option__b7Uwf']//a[contains(@href,'/topics')]")))
            Others = driver.find_elements(By.XPATH,"//li[@class='styles_option__b7Uwf']//a[contains(@href,'/topics')]")
            Industry_type.extend(Others)
        except:
            pass
            #print("There is only one industry type")
        
        Industry_type.append(elemnt1)

        print(Industry_type)
        print("Below is the list of Industry_type")
        for item in Industry_type:
            print(item.text)



        ## Close the open Window of current Product
        driver.find_element(By.XPATH,"//a[@data-test='modal-close']").click()

