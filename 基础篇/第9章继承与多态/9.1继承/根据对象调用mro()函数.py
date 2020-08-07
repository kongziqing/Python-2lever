"""
使用__class__系统变量还可以根据一个类的实例化对象来获取mro信息
"""
# coding : utf-8
class Base: 					# 定义父类
    pass						# 结构为空
class Parent(Base): 					# 定义Base子类
    pass						# 结构为空
class Message: 					# 定义独立的类
    pass						# 结构为空
class SubA(Parent,Message): 				# 定义Parent与Message子类
    pass						# 结构为空
class SubB(Parent,Message): 				# 定义Parent与Message子类
    pass						# 结构为空

def main():				# 主函数
    sub = SubA()				# 实例化子类对象
    print(sub.__class__.mro())			# 获取mro信息
if __name__ == "__main__":			# 判断执行名称
    main()					# 调用主函数
