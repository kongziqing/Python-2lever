"""
在类中默认定义的方法都需要传入一个当前对象，并且也都需要通过实例化对象进行调用，假设现在一个类中并没有提供任何属性，
但在进行类中方法调用时就必须按照语法要求实例化对象，这样就会造成内存空间的浪费，为了解决这一问题，可以在类中进行静态方法的定义，
这类方法可以直接通过类名称进行调用，并且需要使用@staticmethod装饰器定义

本程序在Message类定义了get_info()静态方法，这样在程序调用时就可以直接采用"类名称.静态方法（）"的形式进行调用
"""

# coding : UTF-8
class Message: 						# 自定义Messsage类
    title = "沐言优拓"					# 定义属性
    @staticmethod                                       		# 静态方法装饰器
    def get_info():                                     		# 定义静态方法
        return "www.yootk.com"					# 返回数据
def main():						# 主函数
    print("%s：%s" % (Message.title, Message.get_info()))		# 信息输出
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
