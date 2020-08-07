"""
注意：关于静态方法的使用限制
在一个类中定义的非静态方法，彼此之间是可以进行互相调用的，但是如果类中定义了静态方法，则静态方法是不允许直接调用非静态方法的，而必须
通过实例化对象的形式完成使用

虽然静态方法定义在了一个类中，但是从严格意义上来讲，它是一个独立的结构体，不受类实例化对象的限制，而在实际的项目开发中，对于类中
的方法首选的还是非静态方法（通过实例化对象调用的方法）。静态方法的定义原则为：类中不定义任何属性并且需要通过类名称调用方法
"""
# coding : UTF-8
class Message: 					# 自定义Message类
    title = "沐言优拓"				# 属性定义
    @staticmethod  					# 静态方法装饰器
    def get_info():					# 定义静态方法
        Message().hello()				# 实例化对象调用静态方法
        return Message.title + "www.yootk.com"		# 返回数据
    def hello(self): 				# 非静态方法
        print("Hello 小李老师")			# 输出提示信息
def main():					# 主函数
    print(Message.get_info())				# 信息输出
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
