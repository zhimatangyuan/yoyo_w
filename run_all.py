# *_*coding:utf-8 *_*
import unittest
from common import HTMLTestRunner_cn

casePath = "F:\\PyCharm Webroot\\web_auto\\case"
rule = "test*.py"

# defaultTestLoader用例加载器
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)


reportPath = "F:\\PyCharm Webroot\\web_auto\\report\\" + "report33.html"

fp = open(reportPath,"wb") # 二进制写入

# 如果失败了想重跑一次，就在最后加参数retry=1
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="报告的title",description="描述你的报告干什么用的",retry=1)

runner.run(discover)
fp.close()

