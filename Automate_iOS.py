import os
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

userName = os.environ.get("BROWSERSTACK_USERNAME")
accessKey = os.environ.get("BROWSERSTACK_ACCESS_KEY")
buildName = os.environ.get("JENKINS_LABEL", "0")

versions = [
{
    "osVersion" : "16",
    "deviceName" : "iPhone 14",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "4.0.0",
    "userName": userName,
    "accessKey": accessKey
}
]

for i in versions:
    print(i['osVersion'])
    options = webdriver.ChromeOptions()
    time.sleep(3)
    options.set_capability('bstack:options', i)
    time.sleep(3)
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
