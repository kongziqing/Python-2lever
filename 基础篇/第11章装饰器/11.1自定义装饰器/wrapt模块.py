"""
在Python提供的标准语法中，如果要使用装饰器，则必须进行函数的嵌套定义，这样使得程序开发逻辑变得复杂，
为了解这个问题，开发者可以利用Python中提供的wrapt模块简化装饰器的定义
"""
# coding : UTF-8
import wrapt						# 模块导入
@wrapt.decorator  						# 使用wrapt模块包装
def logging(wrapped, instance, args, kwargs): 			# 定义装饰器
    print("[Logging]: 进入“{fun}()”".format(fun=wrapped.__name__))	# 输出提示信息
    return wrapped(*args, **kwargs) 				# 返回包装函数引用
class Message: 						# 自定义Message类
    @logging						# 通过装饰器配置
    def print_title(self): 					# 类业务方法
        print("沐言优拓")					# 核心功能
    @logging  						# 通过装饰器配置
    def print_url(self): 					# 类业务方法
        print("www.yootk.com") 				# 核心功能
def main():						# 主函数
    msg = Message()						# 实例化类对象
    msg.print_title()					# 调用业务方法
    msg.print_url()						# 调用业务方法
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
