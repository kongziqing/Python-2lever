"""
利用继承性使得不同的类之间存在关联，对象也会分为父类或子类实例，为了方便获取这些关联结构的信息并对相关继承关系进行判断，
Python提供了许多内置的系统变量与函数用于进行类信息或者相关实例的判断

获取继承结构信息的函数与变量
*__class__   变量  获取指定对象所属类Class对象，与type()返回值相同
*__bases__   变量  获取一个类对应的所有父类信息
*__subclasses__()  函数  获取一个类对应的所有子类信息
*issubclass(clazz,父类)  函数  判断一个Class对象是否是某一类的子类

提问：__class__有什么用？
使用__class__主要是根据对象获取其类型，但是在开发中如果不知道类型，则肯定无法进行对象创建，那么__calss__有什么用？
回答：可以确定类型与获取mro信息
在Python中，由于所有变量没有强制要求进行数据类型定义，所以当通过某些方法接收到返回对象时，有可能造成不明确对象类型而导致程序
代码出错的问题，因而Python提供了"对象.__class__"系统变量和type类以获取类信息，这样在开发中可以结合分支判断进行类型判断并进行准确方法的调用
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

#使用__class__获取类信息
def main():
    sub = SubA()					# 实例化子类对象
    msg = Message()					# 实例化Message类对象
    print("sub对象所属类型：%s" % sub.__class__)		# 根据实例化对象获取其对应类型
    print("msg对象所属类型：%s" % msg.__class__)		# 根据实例化对象获取其对应类型
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
