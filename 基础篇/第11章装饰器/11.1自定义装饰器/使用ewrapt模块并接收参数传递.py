"""
本程序由于logging装饰器需要进行参数的接收，所以在logging()函数内部嵌套了另外一个函数
"""
# coding : UTF-8
import wrapt						# 模块导入
def logging(level="INFO"):					# 定义装饰器
    @wrapt.decorator 					# 使用wrapt模块包装
    def wrapper(wrapped, instance, args, kwargs): 			# 包装函数
        print("[Logging-{lev}]: 进入“{fun}()”".format(
		lev=level, fun=wrapped.__name__))		# 输出提示信息
        return wrapped(*args, **kwargs) 				# 返回包装函数引用
    return wrapper						# 返回函数引用
class Message: 						# 自定义Message类
    @logging(level="DEBUG") 					# 通过装饰器配置
    def print_title(self): 					# 类业务方法
        print("沐言优拓")					# 核心功能
    @logging()						# 通过装饰器配置
    def print_url(self): 					# 类业务方法
        print("www.yootk.com")					# 核心功能
def main():						# 主函数
    msg = Message()						# 实例化类对象
    msg.print_title()					# 调用业务方法
    msg.print_url()						# 调用业务方法
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
