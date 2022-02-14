import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from checkbox import AwesomeApp,SortBy,DatePosted,ExpLevel,JobLevel,Work_Mode

job_page=[]
job_links=[]
total=[]

class LinkedIn_Jobs:

    def __init__(self,link,email,password,field_name,location,Sort_By,Date_Posted,Experienced_Level,Job_Level,OnSite_Remote):
        self.link=link
        self.email=email
        self.password=password
        self.field_name=field_name
        self.location=location
        self.Sort_By=Sort_By
        self.Date_Posted=Date_Posted
        self.Experienced_Level=Experienced_Level
        self.Job_Level=Job_Level
        self.OnSite_Remote=OnSite_Remote


    def login(self):
        ## Launch the browser and navigate to LinkedIn page
        self.driver= webdriver.Chrome("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(self.link)
        self.wait=WebDriverWait(self.driver, 2)
        ## Navigate to Sign-In Page
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='nav__button-secondary']")))
        self.driver.find_element(By.XPATH,'//a[@class="nav__button-secondary"]').click() 

        ## Enter the credentials Email and password
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
        self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(self.email)

        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(self.password)

        self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Sign in"]')))
        self.driver.find_element(By.XPATH,'//button[text()="Sign in"]').click()





    def Search_Field(self):
        
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-test-global-nav-link="jobs"]')))
        self.driver.find_element(By.XPATH,'//a[@data-test-global-nav-link="jobs"]').click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search by title, skill, or company']")))
        self.driver.find_element(By.XPATH,"//input[@aria-label='Search by title, skill, or company']").send_keys(field_name)


        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='City, state, or zip code']")))
        self.driver.find_element(By.XPATH,"//input[@aria-label='City, state, or zip code']").send_keys(location)

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Search']")))
        self.driver.find_element(By.XPATH,"//button[text()='Search']").click()

    


    def Set_Filters(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='All filters']")))
        self.driver.find_element(By.XPATH,"//button[@aria-label='All filters']").click()

        #Sort_By ='Most recent'
        for item in self.Sort_By:
            if item=='Most recent':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-sortBy')]//span[text()='Most recent']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-sortBy')]//span[text()='Most recent']").click()  
            else:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-sortBy')]//span[text()='Most relevant']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-sortBy')]//span[text()='Most relevant']").click()


        #Date_Posted ='Past Month'
        for item in self.Date_Posted:
            if item=='Past Month':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Past Month']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Past Month']").click()
            elif item=='Past Week':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Past Week']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Past Week']").click()
            elif item=='Past 24 hours':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Past 24 hours']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Past 24 hours']").click()    
            else:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Any Time']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-timePostedRange')]//span[text()='Any Time']").click()


        #Experience_Level =['Internship','Entry level','Associate','Mid-Senior level','Director','Executive']
        for item in self.Experienced_Level:
            if item=='Internship':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-experience')]//span[text()='Internship']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-experience')]//span[text()='Internship']").click()
            elif item=='Entry level':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-experience')]//span[text()='Entry level']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-experience')]//span[text()='Entry level']").click()
            elif item=='Associate':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-experience')]//span[text()='Associate']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-experience')]//span[text()='Associate']").click()    
            elif item=='Mid-Senior level':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-experience')]//span[text()='Mid-Senior level']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-experience')]//span[text()='Mid-Senior level']").click()
            elif item=='Director':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-experience')]//span[text()='Director']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-experience')]//span[text()='Director']").click()
            else:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-experience')]//span[text()='Executive']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-experience')]//span[text()='Executive']").click()


        #Job_Type =['Full-time','Part-time','Contract','Temporary','Volunteer','Internship','Other']
        for item in self.Job_Level:
            if item=='Full-time':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Full-time']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Full-time']").click()
            elif item=='Part-time':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Part-time']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Part-time']").click()
            elif item=='Contract':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Contract']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Contract']").click()    
            elif item=='Temporary':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Temporary']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Temporary']").click()
            elif item=='Volunteer':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Volunteer']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Volunteer']").click()
            elif item=='Internship':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Internship']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Internship']").click()    
            else:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-jobType')]//span[text()='Other']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-jobType')]//span[text()='Other']").click()


        #OnSite_Remote=['Hybrid','Remote','On-site']
        for item in self.OnSite_Remote:
            if item=='Hybrid':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-workplaceType')]//span[text()='Hybrid']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-workplaceType')]//span[text()='Hybrid']").click()
            elif item=='Remote':
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-workplaceType')]//span[text()='Remote']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-workplaceType')]//span[text()='Remote']").click()
            else:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@for,'advanced-filter-workplaceType')]//span[text()='On-site']")))
                self.driver.find_element(By.XPATH,"//label[contains(@for,'advanced-filter-workplaceType')]//span[text()='On-site']").click()

        self.driver.find_element(By.XPATH,"//button[contains(@aria-label,'Apply current filters')]").click()
    




    def find_jobs(self):
        Total_Pages=self.driver.find_elements(By.XPATH,"//ul[@class='artdeco-pagination__pages artdeco-pagination__pages--number']//span")
        end_page=int(Total_Pages[-1].text)

        main_url=self.driver.current_url
        job_count=0

        for item in range(0,end_page):
            link=main_url+'&start='+str(job_count)
            job_count=job_count+25
            job_page.append(link)
        
        
        for link in job_page:
            self.driver.get(link)
            for prod in range(1,26):
                try:
                    prod_no = "//ul[contains(@class,'jobs-search-results')]//li[contains(@class,'jobs-search-results')]"+str([prod])
                    self.wait.until(EC.presence_of_element_located((By.XPATH,prod_no)))
                    self.driver.find_element(By.XPATH,prod_no).click()
                except:
                    break
            total=self.driver.find_elements(By.XPATH,"//a[contains(@href,'jobs/view') and contains(@class,'job-card-list__title')]")
            print(len(total))
            if len(total)!=0:
                try:
                    for i in range(len(total)):
                        job_links.append(total[i].get_attribute('href'))
                except:
                    continue







    
    def Scrap_Job_Details(self):
        index=0
        column_names = ["Job_Links"]
        df = pd.DataFrame(columns = column_names)

        for item in range(len(job_links)):
            df.loc[index,:]=job_links[item]
            index=index+1

        df.to_csv("Job_Links.csv")
        jobs=pd.read_csv('Job_Links.csv')



        for item in range(len(jobs)):
            self.driver.get(jobs.loc[item,'Job_Links'])
    
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(@class,'t-bold')]")))
                jobs.loc[item,'Job_title']=self.driver.find_element(By.XPATH,"//h1[contains(@class,'t-bold')]").text
            except:
                jobs.loc[item,'Job_title']='No Job Title found'
              
    
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'bullet')]")))
                jobs.loc[item,'Location']=self.driver.find_element(By.XPATH,"//span[contains(@class,'bullet')]").text
            except:
                jobs.loc[item,'Location']='No Location details found'
    
    
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//span//a[contains(@href,'/company/')]")))
                jobs.loc[item,'Company']=self.driver.find_element(By.XPATH,"//span//a[contains(@href,'/company/')]").text
            except:
                jobs.loc[item,'Company']='No Company details found'
        
        
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'job-insight')][1]//span[1]")))
                jobs.loc[item,'Job_Level']=self.driver.find_element(By.XPATH,"//div[contains(@class,'job-insight')][1]//span[1]").text
            except:
                jobs.loc[item,'Job_Level']='No Job Level details found'
        
        
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'job-insight')]//span[text()='Actively recruiting']")))
                jobs.loc[item,'JobRecruit_Status']=self.driver.find_element(By.XPATH,"//div[contains(@class,'job-insight')]//span[text()='Actively recruiting']").text
            except:
                jobs.loc[item,'JobRecruit_Status']='Not Recruiting Actively'
        
        
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(@class,'jobs-poster__name')]")))
                jobs.loc[item,'Job_Recruiter']=self.driver.find_element(By.XPATH,"//p[contains(@class,'jobs-poster__name')]").text
            except:
                jobs.loc[item,'Job_Recruiter']='No Recruiter details found'


        jobs.to_csv("Job_Details.csv")





if __name__=="__main__":
    
    link='http://www.linkedin.com'
    email=input("Enter the Mail ID: ")
    password=input("Enter the password: ")
    field_name = input("Enter the Field Value: ")
    location = input("Enter the Location: ")
    
    AwesomeApp().run()



    job = LinkedIn_Jobs(link,email,password,field_name,location,SortBy,DatePosted,ExpLevel,JobLevel,Work_Mode)
    job.login()
    job.Search_Field()
    job.Set_Filters()
    time.sleep(2)
    job.find_jobs()
    print(len(job_links))
    job.Scrap_Job_Details()
