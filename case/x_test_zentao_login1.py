# *_*coding:utf-8 *_*
# 2019.03.21 此课重点

from selenium import webdriver
import time
import unittest


class LoginTest(unittest.TestCase):
    '''登录类的注释'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def setUp(self):

        self.driver.get("https://mail.qq.com/")
        # 由于框架问题，python3截图在teardown里会把它清空，所以teardown的内容放在setup
        self.is_alert_exists()
        self.driver.delete_all_cookies()  # 退出登录
        self.driver.refresh()  # 刷新


    # 获取用户名信息
    def get_login_username(self):
        try:
            t = self.driver.find_element_by_id("useralias").text
            print(t)
            return t
        except:
            return ""

    # 判断alert弹窗
    def is_alert_exists(self):
        '''判断alert是不是存在'''
        time.sleep(2)
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept() # 用alert 点alert
            return text
        except:
            return ""

    def login(self,user,password):
        self.driver.switch_to.frame("login_frame")
        self.driver.find_element_by_name("u").send_keys(user)
        self.driver.find_element_by_name("p").send_keys(password)
        self.driver.find_element_by_id("login_button").click()

    def test_01(self):
        '''用例说明：01 账号xxx密码xxx'''
        time.sleep(3)
        self.login("1311289418","zhongguo123456?")

        # 判断是否登陆成功
        time.sleep(3)
        t = self.get_login_username()

        print("获取的结果：%s"%t)
        self.assertTrue(t == "芝麻汤圆")

    def test_02(self):
        '''用例说明：02  账号xxx密码xxx'''
        time.sleep(2)
        # 错误账号和密码
        self.login("31313131","12344")

        # 判断是否登陆成功
        time.sleep(3)
        t = self.get_login_username()
        print("登录失败，获取结果：%s"%t)

        self.assertTrue(t == "") # 断言失败自动截图



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() # 编辑器问题


if __name__ == '__main__':
    unittest.main()
