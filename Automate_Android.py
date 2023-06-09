import os
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

userName = os.environ.get("BROWSERSTACK_USERNAME")
accessKey = os.environ.get("BROWSERSTACK_ACCESS_KEY")
buildName = os.environ.get("JENKINS_LABEL", "Sample Automate test on Android")

versions = [
{
    "osVersion" : "10.0",
    "deviceName" : "Samsung Galaxy S20",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "4.0.0",
    "userName": userName,
    "accessKey": accessKey
},
    {
    "osVersion" : "9.0",
    "deviceName" : "Google Pixel 3",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "4.0.0",
    "userName": userName,
    "accessKey": accessKey
    },
    {
    "osVersion" : "11.0",
    "deviceName" : "OnePlus 9",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "4.0.0",
    "userName": userName,
    "accessKey": accessKey
    },
    {
    "osVersion" : "11.0",
    "deviceName" : "Xiaomi Redmi Note 11",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "4.0.0",
    "userName": userName,
    "accessKey": accessKey
    }
]

for i in versions:
    print(i['deviceName'])
    options = webdriver.ChromeOptions()
    options.set_capability('bstack:options', i)
    driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub",
    options=options)
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://www.browserstack.com/")
    time.sleep(3)
    #driver.find_element("name", "q").send_keys("BrowserStack")
   
    driver.close()
    driver.quit()
    print('test finish')
