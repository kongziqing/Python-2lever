"""
在默认情况下程序执行unittest.main()以启动测试类中的全部测试方法（按照名称顺序执行测试），如果希望某些测试方法不被执行，
则可以通过@unittest.skip装饰器跳过测试操作

此时在进行测试启动时将跳过Math。sub()同时也会输出响应的跳过提示信息
"""
# coding : UTF-8
from yootk_math import Math			# 导入模块组件
import unittest				# 模块导入
class TestMath(unittest.TestCase): 		# 定义测试类
    def test_add(self): 			# 测试add()方法
        self.assertEqual(Math().add(1, 2), 3) 	# 功能测试
    @unittest.skip("Math.sub()方法功能简单，不需要进行测试")
    def test_sub(self): 			# 测试Sub()方法
        self.assertEqual(Math().sub(10, 7), 3) 	# 功能测试
if __name__ == "__main__":			# 判断程序执行名称
    unittest.main()				# 启动测试用例
