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
 'os': 'Windows',
 'os_version': '10',
 'browser': 'chrome',
 'browser_version': 'latest',
 'name': 'BStack-[Jenkins] Sample Test',
 'build': buildName,
 'browserstack.user': userName,
 'browserstack.key': accessKey
},
{
 'os': 'Windows',
 'os_version': '10',
 'browser': 'firefox',
 'browser_version': 'latest',
 'name': 'BStack-[Jenkins] Sample Test',
 'build': buildName,
 'browserstack.user': userName,
 'browserstack.key': accessKey
}
]

for i in versions:
    print(i['browser'])
    driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub",
    desired_capabilities=i)
    
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
    print('Test fini')
