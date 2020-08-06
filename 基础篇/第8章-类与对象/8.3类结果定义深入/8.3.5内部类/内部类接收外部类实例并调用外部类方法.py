"""
内部类与外部类虽然属于嵌套关系，但是两个类彼此还属于完全独立的状态，如果想在内部类中调用外部类
的方法，那么必须将外部类的对象实例传递到内部类中。

本程序在外部类的fun()方法中实例化了Inner类对象，并且将当前实例self传入了inner内部类，这样在Inner类中就可以
依靠外部类的实例调用get_info()方法获得info对象属性内容


"""
# coding : utf-8
class Outer: 					# 自定义外部类
    def __init__(self): 				# 外部类构造方法初始化属性内容
        self.__info = "www.yootk.com" 			# 定义外部类实例属性
    def get_info(self): 				# 外部类定义获取info属性内容
        return self.__info				# 返回info属性内容
    class __Inner: 					# 自定义内部类
        def __init__(self, out): 			# 内部类实例化时接收外部类实例
            self.__out = out  				# 外部类实例作为内部类实例属性保存
        def print_info(self): 				# 内部类方法
            print(self.__out.get_info())			# 通过外部类实例调用外部类方法
    def fun(self): 					# 外部类方法
        inobj = Outer.__Inner(self) 			# 实例化内部类实例并传入外部类当前实例
        inobj.print_info()  				# 内部类对象调用内部类方法
def main():					# 主函数
    out = Outer()    				# 实例化外部类对象
    out.fun()   					# 调用外部类方法
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
