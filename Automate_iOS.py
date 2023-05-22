import os
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

userName = os.environ.get("BROWSERSTACK_USERNAME")
accessKey = os.environ.get("BROWSERSTACK_ACCESS_KEY")
buildName = os.environ.get("JENKINS_LABEL", "Sample Automate test on iOS")

versions = [
# {
#     "osVersion" : "16",
#     "deviceName" : "iPhone 14",
#     "sessionName" : "BStack Build Name: " + buildName,
#     "seleniumVersion" : "4.0.0",
#     "browserName" : "Chrome",
#     "userName": userName,
#     "accessKey": accessKey
# }
# },
# {
#     "osVersion" : "16",
#     "deviceName" : "iPhone 14 Pro Max",
#     "sessionName" : "BStack Build Name: " + buildName,
#     "seleniumVersion" : "4.0.0",
#     "userName": userName,
#     "accessKey": accessKey
# },
# {
#     "osVersion" : "14",
#     "deviceName" : "iPad Air 4",
#     "sessionName" : "BStack Build Name: " + buildName,
#     "seleniumVersion" : "4.0.0",
#     "userName": userName,
#     "accessKey": accessKey
# },
{
    "osVersion" : "13",
    "deviceName" : "iPad Pro 12.9 2020",
    "browserName" : "Chrome",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "4.0.0",
    "userName": userName,
    "accessKey": accessKey
}
]

for i in versions:
    print(i['deviceName'])
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
    driver.close()
    print('test finish')
    #driver.find_element("name", "q").send_keys("BrowserStack")
    
driver.quit()

    
   
    
