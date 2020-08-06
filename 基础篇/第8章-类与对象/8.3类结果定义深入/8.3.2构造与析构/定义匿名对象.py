"""
一个类的对象实例化之后往往会引用一块内存空间，这样就可以使用该实例化对象进行类中方法的重复调用，但在某些时候，某个
实例化对象可能只只用一次，所以就可以省略对象名称的定义，直接通过一个匿名对象进行类中的结构的调用，由于匿名对象
没有引用名称，所以该对象只允许使用一次，之后将成为垃圾空间。

本程序直接利用构造方法创建了以Member类的匿名对象，并直接使用此匿名对象调用了get_info()函数，由于匿名对象没有名称引用，
所以该对象使用一次之后就将成为垃圾空间等待资源释放
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

def main():					# 主函数
    print(Member(name="小李老师",age=18).get_info())	# 信息输出
if __name__ == "__main__":				# 判断程序执行名称
    main()
