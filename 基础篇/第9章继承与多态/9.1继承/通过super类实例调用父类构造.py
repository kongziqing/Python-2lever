"""
本程序在子类构造方法中使用super()实例化对象调用了父类中的无参构造方法，这样一来会先执行父类的构造方法为父类实例初始化，而后在调用
子类构造进行初始化操作
"""
# coding : utf-8
class Parent: 					# 定义Parent类
    def __init__(self): 				# 定义父类构造方法
        print("【Parent父类】__init__()")		# 输出提示信息
class Sub(Parent): 					# 定义子类
    def __init__(self): 				# 定义子类构造方法
        super().__init__()				# 调用父类无参构造
        print("【Sub子类】__init__()")			# 输出提示信息
def main():					# 主函数
    sub = Sub()					# 实例化子类对象
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
