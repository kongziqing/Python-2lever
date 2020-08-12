# coding : UTF-8
from yootk_math import Math			# 导入模块组件
import unittest				# 导入模块
class TestMath(unittest.TestCase): 		# 定义测试类
    @classmethod				# 类方法
    def setUpClass(self): 			# 全局前置处理
        print("【unittest】程序测试开始。")	# 提示信息
    @classmethod				# 类方法
    def tearDownClass(self): 			# 全局后置处理
        print("【unittest】程序测试全部结束。")	# 提示信息
    def tearDown(self): 			# 每个测试用例执行之后做操作
        print("【%s】测试结束" % self.id())	# 提示信息
    def setUp(self): 			# 每个测试用例执行之前做操作
        print("【%s】测试开始" % self.id())	# 提示信息
    def test_add(self): 			# 测试add()方法，必须以“testXxx()”命名
        self.assertEqual(Math().add(1, 2), 3) 	# 功能测试
    def test_sub(self): 			# 测试Sub()方法，必须以“testXxx()”命名
        self.assertEqual(Math().sub(10, 7), 3) 	# 功能测试
if __name__ == "__main__":			# 判断程序执行名称
    unittest.main()				# 启动测试用例
