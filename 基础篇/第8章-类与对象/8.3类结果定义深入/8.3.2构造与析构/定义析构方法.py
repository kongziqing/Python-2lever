"""
除了构造方法之外，还可以在类中定义析构方法，析构方法的主要作用在于对象回收前的资源释放操作，
在Python中的析构方法的名称为__del__(),当一个对象不再使用或者使用了del关键字删除对象时，
都会自动调用析构方法。
本程序在Member类中定义了析构方法，可以发现当一个对象不再使用或者使用del明确删除对象时都会自动进行析构方法的调用
"""
class Member: 						# 自定义Member类
    def __init__(self,**kwargs): 				# 构造方法接收所需要的参数
        print("【构造方法】实例化新对象，当前对象地址：%s" % id(self)) 	# 输出提示信息
        self.__name = kwargs.get("name")				# 为name属性初始化
        self.__age = kwargs.get("age")				# 为age属性初始化
    def __del__(self):           				# 定义析构方法
        print("〖析构方法〗资源被释放，当前对象地址：%s" % id(self)) 	# 输出提示信息
    def get_info(self): 					# 获取对象信息
        return "姓名：%s、年龄：%s" % (self.__name,self.__age) 	# 获返回属性内容
    # setter、getter相关方法、略
def main():						# 主函数
    mem_a = Member()						# 无参构造
    mem_b = Member(name="小李老师",age=18) 			# 有参构造
    print("mem_a对象内存地址：%s、mem_b对象内存地址：%s" % (id(mem_a),id(mem_b))) # 获取对象地址
    del mem_b 						# 显示调用析构方法
    print(mem_a.get_info())					# 信息输出
if __name__ == "__main__":					# 判断程序执行名称
    main()
