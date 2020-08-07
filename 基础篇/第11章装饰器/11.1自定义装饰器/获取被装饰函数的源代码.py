"""
在进行装饰器绑定的过程中，也可以使用inspect模型中的getsource()函数获取被装饰程序的源代码
"""
def logging(func): 				# 接收一个函数作为参数
    def wrapper(*args, **kwargs): 		# 定义装饰
        print("[Logging-INFO]: 进入“{fun}()”".format(fun=func.__name__))# 提示信息
        import inspect			# 模块导入
        print(inspect.getsource(func)) 		# 获取操作源代码
        return func(*args, **kwargs) 		# 装饰器内部调用原函数要带星号
    return wrapper 				# 返回装饰器函数引用
class Message: 						# 自定义Message类
    @logging 						# 通过装饰器配置
    def print_title(self): 					# 类业务方法
        print("沐言优拓")					# 核心功能
    @logging    						# 通过装饰器配置
    def print_url(self): 					# 类业务方法
        print("www.yootk.com") 				# 核心功能
def main():						# 主函数
    msg = Message()						# 实例化类对象
    msg.print_title()					# 调用业务方法
    msg.print_url()						# 调用业务方法
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
