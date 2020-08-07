"""
除了__str__()方法之外，在object类中又提供了一个__repr__()方法，该方法也可以获取对象信息，但是需要通过repr()函数转换后才可以执行
本程序在Message类中覆写了__repr__()方法，这样在输出对象时用户只要通过repr()转换函数执行后就可以对该方法实现自动调用
"""
# coding : utf-8
class Message: 				# 默认object子类
    def __init__(self,content): 		# 构造方法初始化内容
        self.__content = content		# 覆写特殊方法
    def __str__(self): 			# 覆写object类方法
        return "【__str__()】%s" % self.__content	# 返回对象信息
    def __repr__(self): 			# 覆写特殊方法
        return "【__repr__()】%s" % self.__content	# 返回对象信息
def main():				# 主函数
    msg = Message("www.yootk.com") 		# 实例化类对象
    print(str(msg)) 				# 不使用str()函数也表示调用“__str__()”
    print(repr(msg)) 			# 必须使用repr()函数才可以调用“__repr__()”
if __name__ == "__main__":			# 判断程序执行名称
    main()					# 调用主函数
