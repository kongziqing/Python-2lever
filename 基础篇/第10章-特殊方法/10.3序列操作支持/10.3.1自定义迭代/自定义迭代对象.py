"""
序列结构可以直接使用for循环进行迭代输出，在自定义类中也可以直接利用如下的方法定义可迭代输出的类
1.__iter__(self)  序列遍历
2.__next__(self)  从迭代器中获取数据
本程序在Message类中定义了迭代操作支持，由于在使用for循环进行输出是必须输出一个可迭代对象，所以需要通过__iter__()方法
返回当前对象，随后自动调用__next__()方法获取所需要的的迭代内容
"""

# coding : utf-8
class Message: 						# 默认继承object类
    def __init__(self, max): 					# 构造方法
        self.__max = max 					# 设置生成数据的最大值
        self.__foot = 0 					# 操作脚标
    def __iter__(self): 					# 返回迭代对象
        return self    					# 当前对象为可迭代对象
    def __next__(self): 					# 获取内容
        if (self.__foot >= self.__max): 				# 结束判断
            return -1					# 结束标记
        else: 						# 还有数据
            val = self.__max - self.__foot			# 获取当前迭代数据
            self.__foot += 1 					# 修改脚标
            return val					# 返回数据
def main():						# 主函数
    msg = Message(10) 					# 实例化类对象
    for v in msg: 						# 对象可以直接进行迭代
        if (v == -1): 					# 定义结束标记
            break						# 退出循环
        print(v, end="、")					# 输出数据
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
