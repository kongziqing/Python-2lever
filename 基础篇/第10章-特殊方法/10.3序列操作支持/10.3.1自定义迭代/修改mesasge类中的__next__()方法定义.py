"""
提问：为什么要在for语句中使用break操作
在本程序实现自定义迭代结构中，为什么需要在外部的for循环中有一个break操作以结束迭代处理呢？这样的操作在之前序列迭代输出中没有出现过，
那么这是不是可以说自定义迭代的功能不如序列迭代的功能强呢？

回答：可以通过异常抛出来解决当前问题
当前的迭代操作中出现的break结束语句，只需要修改__next__()方法就可以将其取消
"""
class Message: 						# 默认继承object类
    def __init__(self, max): 					# 构造方法
        self.__max = max 					# 设置生成数据的最大值
        self.__foot = 0 					# 操作脚标
    def __iter__(self): 					# 返回迭代对象
        return self    					# 当前对象为可迭代对象
    def __next__(self): 					# 获取内容
        if (self.__foot >= self.__max): 				# 结束判断
            raise StopIteration					# 结束标记
        else: 						# 还有数据
            val = self.__max - self.__foot			# 获取当前迭代数据
            self.__foot += 1 					# 修改脚标
            return val					# 返回数据
def main():						# 主函数
    msg = Message(10) 					# 实例化类对象
    for v in msg: 						# 对象可以直接进行迭代
        print(v, end="、")					# 输出数据
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
