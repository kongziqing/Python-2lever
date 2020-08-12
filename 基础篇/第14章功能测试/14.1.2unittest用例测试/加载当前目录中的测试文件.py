"""
提问：测试文件过多时可以自动执行吗？
一个项目中往往会存在大量的程序测试文件，那么这些测试文件需要一个一个执行吗？Python有没有提供自动执行全部测试文件的支持

回答：未提供原生支持，可以自行实现
在编写屙屎代码时往往会将测试文件保存在同一路径下，这样就可以利用通配符加载与执行测试文件

本程序利用os模块获取了当前程序的工作目录，随后加载并执行了所有以“test”前缀命名的测试文件进行测试功能的说明
"""
# coding : UTF-8
import os, unittest			# 模块导入
class RunAllTest(unittest.TestCase): 	# 定义测试类
    def test_run(self): 		# 测试函数
        case_path = os.getcwd()	# 获取目录
        # 目录进行测试文件的名称匹配，以“test_”开头的均为测试文件
        discover = unittest.defaultTestLoader.discover(
                case_path, pattern="test_*.py")
        # 详细程度控制，内容包括：0（简单）、1（默认值）、2（详细）
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(discover) 		# 运行测试
if __name__=='__main__': 		# 判断程序执行名称
    unittest.main()			# 启动测试用例

