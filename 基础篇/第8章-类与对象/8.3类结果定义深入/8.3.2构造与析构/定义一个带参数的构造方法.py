"""
类中提供构造方法的主要目的是方便类中的属性初始化，所以也可以通过__init__()函数接收参数，
这样就可以在类对象实例化时为类中属性进行初始化，从而避免重复调用setter方法进行设置

本程序在Member类中定义了一个有参构造方法，所以在实例化Member类对象时需要明确地传入两个参数内容，
这样在mem对象实例化时就自动为属性进行了赋值处理
"""

class Member: 					# 自定义Member类
    def __init__(self,name,age): 			# 构造方法接收所需要的参数
        self.__name = name				# 为name属性初始化
        self.__age = age 				# 为age属性初始化
    def get_info(self): 				# 获取对象信息
        return "姓名：%s、年龄：%s" % (self.__name,self.__age) # 返回属性内容
    # setter、getter相关方法、略
def main():					# 主函数
    mem = Member("小李老师",18) 			# 实例化对象并设置属性初始化内容
    print(mem.get_info())				# 调用get_info()方法输出属性内容
if __name__ == "__main__":				# 判断程序执行名称
    main()
