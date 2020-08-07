"""
一个类的实例化对象可以进行类中方法的调用，但是除了 这种标准调用形式之外，Python还提供"对象（）"的形式进行方法调用，
而此种语法的执行需要__call__(self,*args,**kwargs)方法支持，此方法中可以有用户任意地进行所需要的参数传递
本程序在Message类中定义了__call__()方法，表示该类的对象可以直接调用（callable（msg）返回为True，表示可调用），这样
就可以在程序中通过"对象()"的形式接收__call__()方法的返回结果
"""

# coding : UTF-8
class Message: 					# object子类
    def __call__(self, *args, **kwargs): 		# 定义对象调用支持
        return "title = %s、url = %s" % (kwargs.get("title"), kwargs.get("url")) # 返回数据
def main():					# 主函数
    msg = Message()					# 实例化类对象
    print(msg())					# 对象直接调用并且不传递参数
    print(msg(title="沐言优拓",url="www.yootk.com")) 	# 对象调用并传递参数
    print(callable(msg)) 				# 判断当前对象是否可调用
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
