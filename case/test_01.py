# *_*coding:utf-8 *_*
import unittest

class IntegerArithmeticTestCase(unittest.TestCase):

    def test_1(self):
        '''用例说明：1111'''
        print("test_1")
        a = "admin" # 实际结果
        b = "admin1" # 期望结果
        self.assertIn(a,b)

    # def setUp(self):
    #     # 每个用例执行之前，先执行一次
    #     print("先打开浏览器")
    #
    # def tearDown(self):
    #     # 用例执行完之后，调用一次
    #     print("关闭浏览器")

    def testAdd(self):  # test method names begin with 'test'
        '''用例说明：Add'''
        print("Add")
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def test_a(self):
        '''用例说明：aaa'''
        print("a")
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)


if __name__ == '__main__':
    unittest.main()