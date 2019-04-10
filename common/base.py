# *_*coding:utf-8 *_*
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class Base():

    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElementNew(self,locator):
        '''定位到元素，返回元素对象，没定位到，返回Timeout异常'''
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator)(driver))
        return ele

    def findElement(self,locator):
        ele1 = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
        return ele1

    # 需要有配置文件 不完整的代码
    def findElements(self,locator):
        ele1 = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
        return ele1


    def sendKeys(self,locator,text):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self,locator):
        '''判断元素是否被选中，返回bool值'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElemetExist(self,locator):
        '''判断元素是否存在'''
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def isElemetExist2(self,locator):
        '''复数定位elements根据定位的元素个数。判断是否存在某个元素'''
        eles = self.findElements(locator)
        n = len(eles) # 计算元素个数
        if n == 0:
            print("%s" %n)
            return False
        elif n == 1:
            print("%s" % n)
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self,locator):
        '''获取文本'''
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取text失败，返回空")
            return ""

    def is_title(self,_title):
        '''判断页面标题是否一致，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False


    def is_title_contains(self,_title):
        '''判断当前标题是否包含预期字符串，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self,locator,_text):
        '''判断某个元素中的text是否包含了预期的字符串，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False

    def is_value_in_element(self,locator,_value):
        '''判断某个元素中的value属性是否包含了预期的字符串，返回bool值，value为空字符串，返回False'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element_value(locator, _value))
            return result
        except:
            return False

    def is_alert(self):
        '''判断页面上是否存在alert'''
        try:
            result = WebDriverWait(self.driver, 3, self.t).until(
                EC.alert_is_present())
            return result
        except:
            return False

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        ele = self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def select_by_index(self,locator,index=0):
        '''通过索引，index是索引第几个，从0开始，默认选第一个'''
        element = self.findElement(locator) # 定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        '''通过value属性'''
        element = self.findElement(locator) # 定位select这一栏
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        '''通过文本值属性'''
        element = self.findElement(locator) # 定位select这一栏
        Select(element).select_by_visible_text(text)

    def is_focus_element(self,locator):
        '''聚焦元素'''
        target = driver.find_element(locator)
        driver.execute_script("arguments[0].scrollIntoView();",target)

    def is_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)

    def is_scroll_end(self,x=0):
        '''滚动到底部,x为横向滚动'''
        js = "window.scrollTo(%s,document.body.scrollHeight)"%x
        driver.execute_script(js)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://mail.qq.com")
    zentao = Base(driver)
    driver.switch_to.frame("login_frame")

    loc1 = (By.NAME, "u")
    loc2 = (By.NAME, "p")
    loc3 = (By.ID, "login_button")

    # 另一种方式，不用导入BY
    # loc1 = ("name", "u")
    # loc2 = ("name", "p")
    # loc3 = ("id", "login_button")

    zentao.sendKeys(loc1,"1311289418")
    zentao.sendKeys(loc2,"zhongguo123456?")
    zentao.click(loc3)
    driver.quit()

