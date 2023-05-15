import os
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

username = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
build_name = os.getenv("BROWSERSTACK_BUILD_NAME")

v1 = {
"os_version" : "16",
"device" : "iPhone 14",
"browserstack.local" : "false",
'name': 'BStack-[Jenkins] Sample Test',
'build': build_name,
'browserstack.user': username,
'browserstack.key': access_key
}


driver = webdriver.Remote(
    command_executor='https://hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=v1)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element("name", "q").send_keys("BrowserStack")
time.sleep(3)
try:
    print('pressing enter on iphone14')
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
