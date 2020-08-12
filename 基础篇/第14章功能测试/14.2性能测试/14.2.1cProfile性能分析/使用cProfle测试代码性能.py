"""
cProfile是一个由c语言编写的Python性能测试模块，利用它可以方便地对代码的执行性能进行分析，但是cProfile只是对程序
代码占用的CPU时间进行统计，并不关心内存消耗与其他与内存相关联的信息
本程序带入了cProfile函数，随后利用该模块中提供的run()方法调用accumulation()函数

相应的统计信息的含义如表所示:
1.ncalls    函数调用次数
2.tottime    函数总共运行时间
3.percall   函数运行一次的平均时间，等同于'tottime/ncalls'
4.cumtime   函数总计运行时间
5.filename:lineno(function)     函数所在的文件名称、代码行号，函数名
"""
# coding : UTF-8
import cProfile				# 模块导入
def accumulation(num): 			# 定义一个累加操作函数
    sum = 0				# 保存累加结果
    for item in range(num): 			# 迭代
        sum += item				# 数据累加
    return sum				# 返回计算结果
if __name__ == "__main__" : 			# 判断程序执行名称
    cProfile.run("accumulation(109999990)") 	# 调用cProfile测试方法
