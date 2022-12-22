from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/bailasha/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)   #service is the property
driver.get("https://rahulshettyacademy.com")
print(driver.title)
driver.close()



