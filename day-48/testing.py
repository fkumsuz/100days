
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver= webdriver.Chrome(options=chrome_option)
import
driver.get("https://secure-retreat-92358.herokuapp.com/")   
first_name = "Can"
last_name = "Simit"
email = "Scan@gmail.com"
 
first_area= driver.find_element(By.NAME,value='fName') 
first_area.send_keys(first_name ) 
lastname_area= driver.find_element(By.NAME,value='lName') 
lastname_area.send_keys(last_name) 
email_area= driver.find_element(By.NAME,value='email') 
email_area.send_keys(email,Keys.ENTER) 


def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Kalan süre: {i} saniye", end="\r")
        time.sleep(1)
    print("Süre doldu!")

countdown(300)
 