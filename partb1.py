import time
timestamp=time.strftime('%d%m%y-%H%M%S')
from selenium import webdriver

driver=webdriver.Chrome("C:\\Driver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("C:\\Users\\sandy\\PycharmProjects\\Practice\\loginpage.html")
driver.save_screenshot("ScreenshotBeforeEnteringTheValue"+timestamp+".png")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_id("User").send_keys("admin")
driver.find_element_by_id("Pass").send_keys("root123")
driver.save_screenshot("ScreenshotAfterEnteringTheValidValues"+timestamp+".png")
driver.find_element_by_id("btn").click()
driver.save_screenshot("ScreenshotforLoginSuccessfull"+timestamp+".png")
driver.implicitly_wait(5)
driver.get("C:\\Users\\sandy\\PycharmProjects\\Practice\\loginpage.html")
driver.find_element_by_id("User").send_keys("admin1")
driver.find_element_by_id("Pass").send_keys("1234")
driver.save_screenshot("ScreenshotAfterEnteringTheInvalidValues" + timestamp + ".png")
driver.find_element_by_id("btn").click()
driver.switch_to_alert().accept()
driver.save_screenshot("ScreenshotforLoginUnSuccessfull" + timestamp + ".png")
driver.implicitly_wait(5)
driver.quit()