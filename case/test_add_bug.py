# *_*coding:utf-8 *_*
# 2019.03.27 16:53 禅道讲解的测试用例
import unittest
from selenium import  webdriver
from pages.add_bug_page import AddBugPage
from pages.login_page import LoginPage
import time

class Test_Add_Bug(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.bug = AddBugPage(cls.driver)
        cls.a = LoginPage(cls.driver)
        cls.driver.maximize_window()
        cls.a.login()

    def test_add_bug(self):
        timestr = time.strftime("%Y_%m_%d %H:%M:%S")
        title = "测试提交BUG再2" + timestr
        self.bug.add_bug(title)
        time.sleep(4)
        result = self.bug.is_add_bug_success(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()