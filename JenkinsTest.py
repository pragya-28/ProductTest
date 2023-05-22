import os
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

username = os.environ.get("BROWSERSTACK_USERNAME")
accessKey = os.environ.get("BROWSERSTACK_ACCESS_KEY")
buildName = os.environ.get("JENKINS_LABEL", "Parallel Testing: Sample Test")

versions = [
{
    "os" : "Windows",
    "osVersion" : "11",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "3.14.0",
    "browserVersion" : "latest-beta",
    "browserName" : "Chrome",
    "userName": username,
    "accessKey": accessKey
},
{
    "os" : "Windows",
    "osVersion" : "10",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "3.10.0",
    "browserVersion" : "latest",
    "browserName" : "Firefox",
    "userName": username,
    "accessKey": accessKey
},
{
    "os" : "Windows",
    "osVersion" : "8.1",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "3.5.2",
    "browserVersion" : "109.0",
    "browserName" : "Edge",
    "userName": username,
    "accessKey": accessKey
},
{
    "os" : "OS X",
    "osVersion" : "Ventura",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "3.14.0",
    "browserVersion" : "16.0",
    "browserName" : "Safari",
    "userName": username,
    "accessKey": accessKey
},
# Test case FAILED for IE open #
{
    "os" : "Windows",
    "osVersion" : "7",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "3.5.2",
    "browserVersion" : "11.0",
    "browserName" : "IE",
    "userName": username,
    "accessKey": accessKey
}
# Test case FAILED for IE closed #
]

for i in versions:
    print(i['browserName'])
    options = webdriver.ChromeOptions()
    options.set_capability('bstack:options', i)
    driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub",
    options=options)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.find_element("name", "q").send_keys("BrowserStack")
    time.sleep(3)
    try:

        driver.find_element("name", "btnK").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Sample test case successful"}}'
        )
    except Exception as err:
        message = "Exception: " + "btnK was not found for CHROME"
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": '
            + json.dumps(message)
            + "}}"
        )
    driver.close()
    driver.quit()
    print('test finish')
