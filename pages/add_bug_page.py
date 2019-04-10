# *_*coding:utf-8 *_*
# 2019.03.27 15:48 禅道案例讲解

from selenium import webdriver
from common.base import Base
import time

class AddBugPage(Base): # 继承

    # 添加BUG
    loc_test = ("link text","测试") # 测试Tab
    loc_bug = ("link text","Bug") # Bug按钮
    loc_addbug = ("xpath",".//*[@id='createActionMenu']/a") # 点提Bug
    loc_truck = ("xpath",".//*[@id='openedBuild_chosen']/ul") #点击版本
    loc_truck_add = ("xpath",".//*[@id='openedBuild_chosen']/div/ul/li") # 选择版本
    loc_input_title = ("id","title") # 标题
    # 需要先切换iframe
    loc_input_body = ("class name","article-content") # 正文
    loc_save = ("css selector","#submit") # 点击提交

    # 新增的列表
    loc_new = ("xpath",".//*[@id='bugList']/tbody/tr[1]/td[4]/a")


    def add_bug(self, title):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)

        self.sendKeys(self.loc_input_title,title)
        # 输入body
        self.driver.switch_to_frame(0) # 通过下标切换iframe
        self.clear(self.loc_input_body)
        body = '''[测试步骤]xxx
        [结果xxx]
        [期望结果]xxx
        '''
        self.sendKeys(self.loc_input_body,body)
        self.driver.switch_to_default_content()

        self.click(self.loc_save)

    def is_add_bug_success(self,_text):
        return self.is_text_in_element(self.loc_new,_text)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    bug = AddBugPage(driver)

    from pages.login_page import LoginPage
    a = LoginPage(driver)
    a.login()

    timestr = time.strftime("%Y_%m_%d %H:%M:%S")
    title = "测试提交BUG" + timestr
    bug.add_bug(title)
    result = bug.is_add_bug_success(title)
    print(result)

