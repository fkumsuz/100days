from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver= webdriver.Chrome(options=chrome_option)

driver.get("https://www.python.org/")
upcoming_date = driver.find_elements(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[*]/time') 
# for date in upcoming_date:
#     dt_object = datetime.fromisoformat(date.get_attribute("datetime"))
#     formatted_date = dt_object.strftime('%Y-%m-%d') 
#     print(formatted_date)

# driver.quit() 

upcoming_event = driver.find_elements(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[*]/a') 
# for event in upcoming_event:
#     event_name = event.get_attribute("text") 
#     print(event_name)
date_event={}
i=0
for date, event in zip(upcoming_date, upcoming_event):
    event_date_dict={}
    dt_object = datetime.fromisoformat(date.get_attribute("datetime"))
    formatted_date = dt_object.strftime('%Y-%m-%d') 
    event_name = event.get_attribute("text") 
    # print(formatted_date,event_name)  
    # date_event[formatted_date]=event_name
    event_date_dict["time"]=formatted_date
    event_date_dict["name"]=event_name
    date_event[i]=event_date_dict
    i=i+1
    
 
 
print(date_event)
# {'2024-05-04': 'TOUFU - Parent-Child Python Programming Workshop', 
#  '2024-05-05': 'TOUFU - Parent-Child Python Programming Workshop',
#  '2024-05-06': 'TOUFU - Parent-Child Python Programming Workshop', 
#  '2024-05-07': 'May Helsinki Python meetup',
#  '2024-05-15': 'PyCon US 2024'}