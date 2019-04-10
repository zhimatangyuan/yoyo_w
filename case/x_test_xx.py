# *_*coding:utf-8 *_*
# 2019-04-09 00:03  ddt与excel结合

from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
import ddt
from common.read_excel import ExcelUtil
import os

'''
1.输入admin，输入密码123456 点登陆  期望结果
2.输入admin，输入密码  点登陆
3.输入admin111，输入密码123456， 点记住密码按钮  点登陆
'''

# 测试的数据
# testdates = [
#     {"user":"admin","psw":"123456","expect":True},
#     {"user":"admin","psw":"","expect":False},
#     {"user":"admin111","psw":"123456","expect":False},
#
# ]

propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) # 当前工程路径
filepath = os.path.join(propath,"common","datas2.xlsx")
print(filepath)
data = ExcelUtil(filepath)
testdates = data.dict_data()
print(testdates)

@ddt.ddt
class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.loginp = LoginPage(cls.driver)
        cls.driver.get(login_url)

    def setUp(self):
        self.loginp.is_alert_exists()
        self.driver.delete_all_cookies()  # 清除缓存
        self.driver.refresh()  # 刷新
        self.driver.get(login_url)
        # 由于框架问题，python3截图在teardown里会把它清空，所以teardown的内容放在setup


    def login_case(self,user,psw,expect):
        '''参数化登录用例的方法'''
        self.loginp.input_user(user)
        self.loginp.input_psw(psw)
        self.loginp.click_login_button()
        result = self.loginp.get_login_result(user)
        if expect == "True":
            expect_result = True
        else:
            expect_result = False
        print("get的result：%s"%result)
        print("期望为:%s"%expect_result)
        self.assertTrue(result == expect_result)

    @ddt.data(*testdates)
    def test_01(self,data):
        '''1.输入admin，输入密码123456 点登陆'''
        print("------------------------开始测试------------")
        print("测试数据 %s" %data)
        self.login_case(data["user"],data["psw"],data["expect"])
        print("------------------------结束：pass！------------")

    # def test_02(self):
    #     '''2.输入admin，输入密码  点登陆'''
    #     print("------------------------开始测试：test_02------------")
    #     data2 = testdates[1]
    #     print("测试数据 %s" % data2)
    #     self.login_case(data2["user"], data2["psw"], data2["expect"])
    #     print("------------------------结束：pass！------------")
    #
    # def test_03(self):
    #     '''3.输入admin111，输入密码123456， 点记住密码按钮  点登陆'''
    #     print("------------------------开始测试：test_03------------")
    #     data3 = testdates[2]
    #     print("测试数据 %s" % data3)
    #     self.login_case(data3["user"], data3["psw"], data3["expect"])
    #     print("------------------------结束：pass！------------")



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()