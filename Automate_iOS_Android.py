import os
from appium import webdriver

userName = os.environ.get("BROWSERSTACK_USERNAME")
accessKey = os.environ.get("BROWSERSTACK_ACCESS_KEY")
buildName = os.environ.get("JENKINS_LABEL", "0")

options = {
    "platformName": "Android",
    "osVersion" : "10.0",
    "deviceName" : "Samsung Galaxy S20",
    "browserName": "Chrome",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "4.0.0",
    "userName": userName,
    "accessKey": accessKey
}

driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub", options)
driver.get('https://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('browserstack')
search_box.submit()
driver.quit()

