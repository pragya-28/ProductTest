from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_name = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
build_name = os.environ.get("JENKINS_LABEL", "0")
app = os.getenv("BROWSERSTACK_APP_ID")

desired_cap = {
    'app': 'com.android.chrome',
    'device': 'Samsung Galaxy S8',
    'build': build_name,
    'appActivity': 'com.google.android.apps.chrome.Main'
}

driver = webdriver.Remote("https://"+user_name+":"+access_key+"@hub-cloud.browserstack.com/wd/hub", desired_cap)

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((MobileBy.ID, "com.android.chrome:id/search_box_text")))
search_box.click()
search_input = wait.until(EC.presence_of_element_located((MobileBy.ID, "com.android.chrome:id/url_bar")))
search_input.send_keys("browserstack.com")
driver.press_keycode(66)
driver.quit()
