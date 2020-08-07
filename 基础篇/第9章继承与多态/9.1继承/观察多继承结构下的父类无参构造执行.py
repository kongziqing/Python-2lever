"""
在子类没有定义任何构造方法的情况下，Python子类对象实例化时会自动调用父类中的构造方法，但是在多继承结构中，由于一个子类存在有多个父类
，就会造成结构调用的二义性，为了解决这个问题，Python专门提供了一个MRO（Method Resolution Order，方法解析顺序）算法，执行时按照从
左到右的原则进行调用

本程序在Sub子类中同时继承了ParentA和ParentB两个父类，并且Sub子类没有定义构造方法，通过输出结果可以发现此时Sub子类执行了ParentsA
类中无参构造方法，如果ParentA类中没有提供无参构造方法 ，在Sub子类将会调用B类中的无参构造方法
"""
# coding : utf-8
class Base: 					# 定义Base父类
    def __init__(self): 				# 无参构造
        print("【Base】__init__()")			# 输出提示信息
class ParentA(Base): 				# 定义ParentA类
    def __init__(self): 				# 无参构造
        print("【ParentA】__init__()")			# 输出提示信息
class ParentB: 					# 定义ParentB类
    def __init__(self): 				# 无参构造
        print("【ParentA】__init__()")			# 输出提示升毫年升毫
class Sub(ParentA,ParentB):  				# 子类不定义构造
    pass						# 子类结构为空
def main():					# 主函数
    sub = Sub()					# 实例化子类对象
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
