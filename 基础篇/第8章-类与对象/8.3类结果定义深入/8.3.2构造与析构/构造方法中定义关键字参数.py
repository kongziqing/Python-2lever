"""
在一个类中永远都会提供构造方法，即使一个类没有明确定义构造方法，系统也会自动为用户
添加一个无参数的并且什么都不做的默认构造方法，但是如果类中已经明确定义了一个构造方法，
则默认无参构造方法将不会自动生成
如果说现在程序要求同时支持有参构造方法和无参构造方法，那么久可以通过关键字参数的形式进行定义

"""
# coding : utf-8
class Member: 				# 自定义Member类
    def __init__(self,**kwargs): 		# 构造方法接收所需要的参数
        self.__name = kwargs.get("name") 	# 为name属性初始化
        self.__age = kwargs.get("age") 		# 为age属性初始化
    def get_info(self): 			# 获取对象信息
        return "姓名：%s、年龄：%s" % (self.__name,self.__age) # 返回对象信息
    # setter、getter相关方法、略
def main():				# 主函数
    mem_a = Member()  			# 无参构造
    mem_b = Member(name="小李老师",age=18) 	# 有参构造
    print(mem_a.get_info())			# 信息输出
    print(mem_b.get_info())			# 信息输出
if __name__ == "__main__":			# 判断程序执行名称
    main()					# 调用主函数
