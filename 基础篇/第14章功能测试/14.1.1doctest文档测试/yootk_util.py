"""
doctest是一种文档编写的形式实现指定程序文件的功能测试，可以模拟交互式Python执行环境下的代码执行方式，同时测试文档可以直接定义在要测试的
函数中
此时程序配置了doctest的测试操作，开发者按照方法执行程序时，会自动测试代码，但是将测试代码直接写在功能函数中会造成代码阅读不便，
为此可以将测试部分的内容单独定义在一个文件中，在程序运行时通过制定的测试文件实现功能测试。
"""
# coding : UTF-8
import doctest                              # 导入测试模块
# 在程序中对于程序的执行部分使用“>>>程序语句”的形式定义，而执行结果可以直接编写
def multiply(v1, v2): 		# 实现乘法计算
    """
    >>> multiply(5, 6)
    30
    >>> multiply("yootk,", 3)
    'yootk,yootk,yootk,'
    """
    return v1 * v2			# 数学计算
def main():			# 主函数
    doctest.testmod(verbose=True)	# verbose=True表示执行测试的时候会输出详细信息
if __name__ == "__main__":		# 判断程序执行名称
    main()				# 调用主函数
