import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup





column_names = ["Job_Links"]
df = pd.DataFrame(columns = column_names)







driver= webdriver.Chrome("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("http://www.linkedin.com")





wait=WebDriverWait(driver, 2)





wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='nav__button-secondary']")))
driver.find_element(By.XPATH,'//a[@class="nav__button-secondary"]').click()

wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("charanrajshetty1993@gmail.com")

wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("Charan@1993")

wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Sign in"]')))
driver.find_element(By.XPATH,'//button[text()="Sign in"]').click()




field_name = input("Enter the Field Value ")
print(field_name)
location = input("Enter the Location ")
print(location)




Sort_By = input("Enter the Sort By Value.Please select any one of 'Most recent' or 'Most relevant' ")
print(Sort_By)




Date_Posted = input("Enter the Date Posted.Please select any one of 'Past Month','Past Week','Past 24 hours','Any Time'")
print(Date_Posted)




Experienced_Level=set()
flag='Yes'
while(flag=='Yes'):
    values = input("Enter the Experience Level.Please chose values in 'Internship','Entry level',''Associate','Mid-Senior level','Director','Executive' : ")
    Experienced_Level.add(values)
    flag=input("Do you wish to enter more options? Please enter Yes or No : ")  
print(Experienced_Level)





Job_Level=set()
flag='Yes'
while(flag=='Yes'):
    values = input("Enter the Job Level.Please chose values in 'Full-time','Part-time','Contract','Temporary','Volunteer','Internship','Other': ")
    Job_Level.add(values)
    flag=input("Do you wish to enter more options? Please enter Yes or No : ") 
print(Job_Level)    




OnSite_Remote=set()
flag='Yes'
while(flag=='Yes'):
    values = input("Enter the Job Level.Please chose values in 'Hybrid','Remote','On-site': ")
    OnSite_Remote.add(values)
    flag=input("Do you wish to enter more options? Please enter Yes or No : ") 
print(OnSite_Remote)








wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-test-global-nav-link="jobs"]')))
driver.find_element(By.XPATH,'//a[@data-test-global-nav-link="jobs"]').click()


wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search by title, skill, or company']")))
driver.find_element(By.XPATH,"//input[@aria-label='Search by title, skill, or company']").send_keys(field_name)


wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='City, state, or zip code']")))
driver.find_element(By.XPATH,"//input[@aria-label='City, state, or zip code']").send_keys(location)

wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Search']")))
driver.find_element(By.XPATH,"//button[text()='Search']").click()




wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='All filters']")))
driver.find_element(By.XPATH,"//button[@aria-label='All filters']").click()




#Sort_By ='Most recent'
if Sort_By=='Most recent':
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-sortBy')]//span[text()='Most recent']")))
    driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-sortBy')]//span[text()='Most recent']").click()  
else:
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-sortBy')]//span[text()='Most relevant']")))
    driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-sortBy')]//span[text()='Most relevant']").click()



#Date_Posted ='Past Month'
if Date_Posted=='Past Month':
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Past Month']")))
    driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Past Month']").click()
elif Date_Posted=='Past Week':
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Past Week']")))
    driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Past Week']").click()
elif Date_Posted=='Past 24 hours':
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Past 24 hours']")))
    driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Past 24 hours']").click()    
else:
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Any Time']")))
    driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Any Time']").click()





#Experience_Level =['Internship','Entry level','Associate','Mid-Senior level','Director','Executive']
for item in Experienced_Level:
    if item=='Internship':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-experience')]//span[text()='Internship']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-experience')]//span[text()='Internship']").click()
    elif item=='Entry level':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-experience')]//span[text()='Entry level']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-experience')]//span[text()='Entry level']").click()
    elif item=='Associate':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-experience')]//span[text()='Associate']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-experience')]//span[text()='Associate']").click()    
    elif item=='Mid-Senior level':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-experience')]//span[text()='Mid-Senior level']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-experience')]//span[text()='Mid-Senior level']").click()
    elif item=='Director':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-experience')]//span[text()='Director']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-experience')]//span[text()='Director']").click()
    else:
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-experience')]//span[text()='Executive']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-experience')]//span[text()='Executive']").click()





#Job_Type =['Full-time','Part-time','Contract','Temporary','Volunteer','Internship','Other']
for item in Job_Level:
    if item=='Full-time':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Full-time']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Full-time']").click()
    elif item=='Part-time':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Part-time']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Part-time']").click()
    elif item=='Contract':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Contract']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Contract']").click()    
    elif item=='Temporary':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Temporary']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Temporary']").click()
    elif item=='Volunteer':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Volunteer']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Volunteer']").click()
    elif item=='Internship':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Internship']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Internship']").click()    
    else:
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Other']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Other']").click()







OnSite_Remote=['Hybrid','Remote','On-site']
for item in OnSite_Remote:
    if item=='Hybrid':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-workplaceType')]//span[text()='Hybrid']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-workplaceType')]//span[text()='Hybrid']").click()
    elif item=='Remote':
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-workplaceType')]//span[text()='Remote']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-workplaceType')]//span[text()='Remote']").click()
    else:
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-workplaceType')]//span[text()='On-site']")))
        driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-workplaceType')]//span[text()='On-site']").click()



driver.find_element(By.XPATH,"//button[contains(@aria-label,'Apply current filters')]").click()
print(len(driver.find_elements(By.XPATH,"//small")))

time.sleep(3)






i=0
if len(driver.find_elements(By.XPATH,"//small"))!=0:
    for prod in range(1,26):
        try:
            prod_no = "//ul[contains(@class,'jobs-search-results')]//li[contains(@class,'jobs-search-results')]"+str([prod])
            prod_link = prod_no+"//a[contains(@href,'jobs/view') and contains(@class,'job-card-list__title')]"
            driver.find_element(By.XPATH,prod_no).click()
            i=i+1
        except:
            break
else:
    print('No jobs found for the filter')




print(i)



total=driver.find_elements(By.XPATH,"//a[contains(@href,'jobs/view') and contains(@class,'job-card-list__title')]")
print(len(total))








index=0
for item in range(len(total)):
    df.loc[index,:]=total[item].get_attribute('href')
    index=index+1


df.to_csv("Job_Links.csv")
jobs=pd.read_csv('Job_Links.csv')


for item in range(len(jobs)):
    driver.get(jobs.loc[item,'Job_Links'])
    
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(@class,'t-bold')]")))
        jobs.loc[item,'Job_title']=driver.find_element(By.XPATH,"//h1[contains(@class,'t-bold')]").text
    except:
        jobs.loc[item,'Job_title']='No Job Title found'
              
    
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'bullet')]")))
        jobs.loc[item,'Location']=driver.find_element(By.XPATH,"//span[contains(@class,'bullet')]").text
    except:
        jobs.loc[item,'Location']='No Location details found'
    
    
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//span//a[contains(@href,'/company/')]")))
        jobs.loc[item,'Company']=driver.find_element(By.XPATH,"//span//a[contains(@href,'/company/')]").text
    except:
        jobs.loc[item,'Company']='No Company details found'
        
        
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'job-insight')][1]//span[1]")))
        jobs.loc[item,'Job_Level']=driver.find_element(By.XPATH,"//div[contains(@class,'job-insight')][1]//span[1]").text
    except:
        jobs.loc[item,'Job_Level']='No Job Level details found'
        
        
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'job-insight')]//span[text()='Actively recruiting']")))
        jobs.loc[item,'JobRecruit_Status']=driver.find_element(By.XPATH,"//div[contains(@class,'job-insight')]//span[text()='Actively recruiting']").text
    except:
        jobs.loc[item,'JobRecruit_Status']='Not Recruiting Actively'
        
        
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(@class,'jobs-poster__name')]")))
        jobs.loc[item,'Job_Recruiter']=driver.find_element(By.XPATH,"//p[contains(@class,'jobs-poster__name')]").text
    except:
        jobs.loc[item,'Job_Recruiter']='No Recruiter details found'



jobs.to_csv("Job_Details.csv")




