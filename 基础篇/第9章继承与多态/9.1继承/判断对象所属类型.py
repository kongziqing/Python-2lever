"""
本程序通过对象所属的类型判断了其是否属于某个类的实例（也可以直接用isinstance()函数判断），这样就可以直接确定对象身份

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
    if sub.__class__ == SubA: 			# 判断对象类型
        print("sub是SubA类的对象实例。")	# 输出提示信息
if __name__ == "__main__":			# 判断执行名称
    main()					# 调用主函数
