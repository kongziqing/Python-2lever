"""
unittest是一种由用户定义的灵活度较高的测试框架，开发者直接利用unittest实现用例测试以判断操作功能是否正确，unittest模块的
常用方法如表
1.setUpClass(self)  [前置处理]整体测试代码执行之前调用
2.tearDownClass(self)  [后置处理]整体测试代码执行之后调用
3.setUp(self)       [前置处理]每个测试用例代码执行之前调用
4.tearDown(self)    [后置处理]每个测试用例代码执行之后哦调用
5.id(self)      获取要测试的方法名称
6.asssertXxx(first,[second,]msg)  对代码执行结果的进行测试

    unittest中的测试有两种形式：TestCase（单个测试功能）、TestSuite(一组测试用例)、所有的测试用例都需要定义在
一个测试类中，同时该类需要继承unittest.TestCase父类
Math类提供有两个数学计算方法，add()与sub(),随后针对此类的功能编写测试程序类
"""

# coding : UTF-8
class Math: 			# 定义工具类
    def add(self, num_a, num_b): 	# 定义操作函数
        return num_a + num_b		# 加法计算
    def sub(self, num_a, num_b): 	# 定义操作函数
        return num_a - num_b		# 减法计算
