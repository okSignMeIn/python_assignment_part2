from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element_by_id("username").send_keys("student")
driver.find_element_by_id("password").send_keys("Password123")
driver.find_element_by_id("submit").click()
loggedInURL = driver.current_url
if(loggedInURL=="https://practicetestautomation.com/logged-in-successfully/"):
    print("Login in test passed")
else:
    print("login test failed")
driver.close()


