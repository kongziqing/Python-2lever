"""
在Python中可以定义构造方法，这样就可以在对象实例化时执行某些操作，在继承关系中，父类和子类同样也可以进行构造方法的定义，
但是此时构造方法的执行需要考虑两种情况
*当父类定义构造方法，但是子类没有定义构造方法时，实例化子类对象会自动调用父类中提供的无参构造方法，如果此时的子类同时继承多个父类，
则按照继承顺序执行无参构造方法
*当子类定义构造方法时，默认不再调用父类中的任何构造方法，但是可以手工调用。

本程序在定义Sub子类时并没有定义任何构造方法，这样在子类对象实例化时将默认调用父类中的无参构造方法，这样就可以为父类中
的属性进行初始化操作，但如果此时子类中定义了构造方法，那么在默认情况下将不会再去调用父类中的无参构造
"""
class Parent: 					# 定义类
    def __init__(self): 				# 定义父类构造方法
        print("【Parent父类】__init__()")		# 提示信息
class Sub(Parent): 					# 定义子类
   pass						# 子类结构为空
def main():					# 主函数
    sub = Sub()					# 实例化子类对象
if __name__ == "__main__":
    main()

