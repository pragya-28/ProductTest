import os
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

username = os.environ.get('BROWSERSTACK_USERNAME')
accessKey = os.environ.get('BROWSERSTACK_ACCESS_KEY')
buildName = os.environ.get('JENKINS_LABEL','0')

bstack_options = {
	{
    "os" : "Windows",
    "osVersion" : "10",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "4.0.0",
    "userName": username,
    "accessKey": accessKey
	},
	{
    "os" : "Firefox",
    "osVersion" : "2.2.1",
    "sessionName" : "BStack Build Name: " + buildName,
    "seleniumVersion" : "4.0.0",
    "userName": username,
    "accessKey": accessKey
	}
}

options = webdriver.ChromeOptions()
options.set_capability('bstack:options', bstack_options)
driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub",
    options=options)

###############################################
print("Sample test case for CHROME started")

#driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.google.com/")

driver.find_element("name","q").send_keys("BrowserStack")
time.sleep(3)

try:

	driver.find_element("name","btnK").send_keys(Keys.ENTER)
	time.sleep(3)
	#print("Sample test case for CHROME successful")
	driver.execute_script(
	   'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Sample test case for CHROME successful"}}')

except Exception as err:
    message = 'Exception: ' + "btnK was not found for CHROME"
    #print(message + "Sample test case for CHROME NOT successful")
    driver.execute_script(
       'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')

driver.close()
driver.quit()

###############################################
# print("Sample test case for FIREFOX started")

# driver = webdriver.Firefox()

# driver.maximize_window()
# driver.get("https://www.google.com/")

# driver.find_element("name","q").send_keys("BrowserStack")
# time.sleep(3)

# driver.find_element("name","btnK").send_keys(Keys.ENTER)
# time.sleep(3)

# try:

# 	driver.find_element("name","btnK").send_keys(Keys.ENTER)
# 	time.sleep(3)
# 	#print("Sample test case for FIREFOX successful")
# 	driver.execute_script(
# 	   'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Sample test case for FIREFOX successful"}}')

# except Exception as err:
#     print (err)
#     message = 'Exception: ' + "btnK was not found for FIREFOX "
#     #print(message + "Sample test case for FIREFOX NOT successful")
#     driver.execute_script(
#        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')

# driver.close()
# driver.quit()
