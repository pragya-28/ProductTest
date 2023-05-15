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
    "os" : "Windows",
    "osVersion" : "10",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "4.0.0",
    "userName": username,
    "accessKey": accessKey
},
{
    "os" : "Windows",
    "osVersion" : "8",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "4.0.0",
    "userName": username,
    "accessKey": accessKey
}
]


for i in versions:
    print(i['os'])
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
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Sample test case for CHROME successful"}}'
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
    print('test fini')
