"""
在继承结构中，由于子类往往拥有比父类更多的功能，所以在开发过程中，使用子类对象并实例化会比较方便，
但是有些时候父类需要通过构造方法对一些属性进行初始化操作，这样就可以通过父类构造方法将参数的内容传递到父类中
"""
# coding : utf-8
class Parent: 				# 定义Parent类
    def __init__(self, name, age): 		# 定义父类构造方法
        self.__name = name 			# name属性初始化
        self.__age = age 			# age属性初始化
    def get_info(self): 			# 获取对象信息
        return "姓名：%s、年龄：%s" % (self.__name, self.__age) # 返回属性内容
class Sub(Parent): 				# 定义子类
    def __init__(self, name, age): 		# 定义子类构造方法
        super().__init__(name, age) 		# 调用父类构造
def main():				# 主函数
    sub = Sub("小李老师", 18) 			# 实例化子类对象
    print(sub.get_info())			# 输出对象信息
if __name__ == "__main__":			# 判断程序执行名称
    main()					# 调用主函数
