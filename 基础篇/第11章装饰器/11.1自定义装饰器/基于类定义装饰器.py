"""
装饰器是一个可以被直接调用的结构，除了在函数中定义装饰器之外，也可以基于类的形式实现，但是此类中要求必须提供__call__()的特殊方法

本程序通过Logging类实现了装饰器的定义，由于装饰器的类是一个可调用的类，所以在Logging类中定义了__call__()方法，并且将装饰器的操作
直接定义在此方法中。
"""

# coding : UTF-8
class Logging: 						# 定义装饰器类
    def __init__(self,level="INFO"):				# 构造方法接收参数
        self.__level = level 					# 保存日志级别
    def __call__(self, func): 					# 接收方法或函数引用
        def wrapper(*args, **kwargs): 				# 装饰器包装
            print("[Logging-{lev}]: 进入“{fun}()”".format(
		lev=self.__level, fun=func.__name__))		# 输出提示信息
            return func(*args, **kwargs)  			# 装饰器内部调用原函数要带星号
        return wrapper  					# 返回方法引用
class Message: 						# 自定义Message类
    @Logging(level="DEBUG")					# 通过装饰器配置
    def print_title(self): 					# 类业务方法
        print("沐言优拓") 					# 核心功能
    @Logging()						# 通过装饰器配置
    def print_url(self): 					# 类业务方法
        print("www.yootk.com")					# 核心功能
def main():						# 主函数
    msg = Message()						# 实例化类对象
    msg.print_title()					# 调用业务方法
    msg.print_url()						# 调用业务方法
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
