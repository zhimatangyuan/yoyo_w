# *_*coding:utf-8 *_*
# 2019-04-08 22:29 POM(page object model页面对象模式)
from selenium import webdriver
import unittest
from pages.add_bug_page import AddBugPage
from pages.login_page import LoginPage
import time

url = "http://127.0.0.1/zentao/my/"

class AddBugCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.bug = AddBugPage(cls.driver)
        cls.driver.maximize_window()
        a = LoginPage(cls.driver)
        a.login()
        # cls.xx = XXPage(cls.driver)   # 页面实例

    def setUp(self):
        self.driver.get(url)

    def test_add_bug(self):
        '''添加BUG'''
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "测试提交BUG" + timestr
        self.bug.add_bug(title)
        result = self.bug.is_add_bug_success(title)
        print(result)
        self.assertTrue(result)

    def test_add_xxx(self):
        '''添加BUG'''
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "测试提交BUG" + timestr
        self.bug.add_bug(title)
        result = self.bug.is_add_bug_success(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()