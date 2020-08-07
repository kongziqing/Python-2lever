"""
类方法是一个可以被类名称直接调用的方法，类方法需要通过@classmethod装饰器声明，同时在类方法中必须要接收一个当前类的参数，
开发者可以依据此参数进行当前类对象的实例化并调用类中的方法
本程序将get_info()方法定义为了类方法，在此方法定义时就必须传入一个class类型的对象，这样开发者就可以直接依据此对象实例化类对象
并调用hello()方法
"""
# coding : UTF-8
class Message: 					# 自定义Message类
    @classmethod 					# 静态方法装饰器
    def get_info(clazz):  				# 定义类方法
        clazz().hello()				# 实例化类对象并调用类方法
    def hello(self): 				# 定义普通方法
        print("Hello 小李老师")			# 输出提示信息
def main():					# 主函数
    Message.get_info()				# 通过类名称直接调用类方法
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
