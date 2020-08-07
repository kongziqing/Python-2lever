"""
本程序在Sub子类中定义了构造方法，所以在对象实例化时将不再调用父类中提供的构造方法，而只调用子类自己定义的构造方法，
如果这个时候需要在子类中调用父类构造，那么可以借助super类的实例化对象完成
"""
class Parent: 					# 类定义
    def __init__(self): 				# 定义父类构造方法
        print("【Parent父类】__init__()")		# 输出提示信息
class Sub(Parent): 					# 定义子类
    def __init__(self): 				# 定义子类构造方法
        print("【Sub子类】__init__()")			# 输出提示信息
def main():					# 主函数
    sub = Sub()					# 实例化子类对象
if __name__ == "__main__":				# 判断程序执行名称
    main()
