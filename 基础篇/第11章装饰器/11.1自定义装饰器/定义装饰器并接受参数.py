"""
以当前的日记记录装饰器为例，在实际开发中，针对日志会存在有不同的级别，如信息（INFO）、调试（DEBUG）、警告（WARNINIG）、
错误（ERROR），这样装饰器在晶配置的时候就需要接收衣蛾日志的解（level）参数，则此时的装饰器代码定义孺子啊

本程序在定义的logging装饰器中设置了一个level参数，考虑到有不设置参数的情况，在logging（）函数里为level设置了默认值，
装饰器操作中需要有一个明确地装饰器对象，所以在logging（）函数内部定义了wrapper（）函数接收装饰器函数方法引用，并在其内部
函数inner_wrapper()中实现了装饰器的功能调用
"""

# coding : UTF-8
def logging(level="INFO"):					# 接收参数
    def wrapper(func): 					# 接收装饰函数引用
        def inner_wrapper(*args, **kwargs): 			# 定义装饰
            print("[Logging-{lev}]: 进入“{fun}()”".format(lev=level,fun=func.__name__))
            return func(*args, **kwargs) 			# 装饰器内部调用原函数要带星号
        return inner_wrapper					# 返回装饰对象
    return wrapper 						# 返回装饰器函数引用
class Message: 						# 自定义Message类
    @logging(level="DEBUG") 					# 通过装饰器配置
    def print_title(self): 					# 类业务方法
        print("沐言优拓") 					# 核心功能
    @logging()  						# 通过装饰器配置
    def print_url(self): 					# 类业务方法
        print("www.yootk.com")  				# 核心功能
def main():						# 主函数
    msg = Message()						# 实例化类对象
    msg.print_title()					# 调用业务方法
    msg.print_url()						# 调用业务方法
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
