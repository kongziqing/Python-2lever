"""
提问：__repr__()和__str__()的作用一样吗？
在项目开发中，如果要获取对象信息，那么直接输出对象，并自动调用类总得__str__()方法是最方便的，为什么还要提供一个__repr__()方法呢？
而且该方法还必须通过repr()函数转换后才可以执行，为什么要有这样的一种定义？

回答：两者用处不同
在Python中，输出对象信息有两种定义形式
用户获取信息：通过__str__()方法返回一个完整的可读性强的信息字符串，这样用户可以直接获得所需要的信息
开发者获取调试信息:通过__repr__()方法获取更完善的调试内容
__repr__()方法的作用在交互模式下比较方便观察


如果一个类中的__repr__()和__str__()两个方法的定义完全相同，实际上也没有必要重复定义，直接进行引用设置即可
"""
class Message: 				# 默认object子类
    def __init__(self,content): 		# 构造方法初始化内容
        self.__content = content		# 覆写特殊方法
    def __str__(self): 			# 覆写object类方法
        return "【__str__()】%s" % self.__content	# 返回对象信息
    __repr__ = __str__
def main():				# 主函数
    msg = Message("www.yootk.com") 		# 实例化类对象
    print(str(msg)) 				# 不使用str()函数也表示调用“__str__()”
    print(repr(msg)) 			# 必须使用repr()函数才可以调用“__repr__()”
if __name__ == "__main__":			# 判断程序执行名称
    main()					# 调用主函数


