import os
import time
import unittest

timestr = time.strftime('%y%m%d-%H%M%S')
from selenium import webdriver


class Count(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Driver\\chromedriver.exe')
        self.driver.get('C:\\Users\\sandy\\PycharmProjects\\Practice\\democount.html')

    def test_login_count(self):
        time.sleep(6)
        textbox = self.driver.find_elements_by_xpath(".//input[@type='text']")
        count7 = 0
        for i in textbox:
            count7 += 1
        print("Total count of textboxes", count7)
        combobox = self.driver.find_elements_by_xpath(".//select")
        count1 = 0
        for j in combobox:
            count1 += 1
        print("Total count of comboboxes", count1)
        radio = self.driver.find_elements_by_xpath(".//input[@type='radio']")
        count2 = 0
        for k in radio:
            count2 += 1
        print("Total count of radio buttons", count2)
        linktext = self.driver.find_elements_by_xpath(".//a")
        count3 = 0
        for l in linktext:
            count3 += 1
        print("Total count of linktexts", count3)
        checkbox = self.driver.find_elements_by_xpath(".//input[@type='checkbox']")
        count4 = 0
        for m in checkbox:
            count4 += 1
        print("Total count of checkboxes", count4)
        submit = self.driver.find_elements_by_xpath(".//input[@type='submit']")
        count5 = 0
        for n in submit:
            count5 += 1
        print("Total count of submit", count5)

        def tearDown(self):
            self.driver.quit()

if __name__ == "__main___":
    unittest.main()
