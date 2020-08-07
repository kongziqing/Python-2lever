"""
在Python中，一个子类可以同时继承多个父类，一个父类也可以同时拥有多个子类，而关于子类与父类的信息可以通过系统变量动态获取
本程序通过Parent.__subclasses__()函数获取了一个子类的列表，这样就可以直接通过类本身明确地获取其子类的信息，而SubAru.__bases__
会通过一个元组保存一个类所继承的所有父类信息。
"""

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

def main():					# 主函数
    print("【Parent子类】%s" % Parent.__subclasses__())	# 获取全部子类
    print("【SubA父类】%s" % str(SubA.__bases__))		# 获取子类父类
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
