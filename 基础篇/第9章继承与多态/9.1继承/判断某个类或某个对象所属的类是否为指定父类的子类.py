"""
由于一个子类可能同时继承有多个父类，这样为了确认某一个类是否为指定父类的子类，可以通过issubclass()函数来进行判断

issubclass()函数是依靠类对象的形式进行判断，如果直接使用类名称判断，那么久可以直接获取类对象，如果使用的是实例化对象，
则必须依靠__class__系统变量获取对应类后才可以进行判断
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

def main():				# 主函数
    sub = SubA()				# 实例化子类对象
    print(issubclass(sub.__class__,Parent)) 	# 通过对象获取类信息并判断是否为指定类的子类
    print(issubclass(SubB,Parent)) 		# 判断是否为指定类的子类
if __name__ == "__main__":			# 判断程序执行名称
    main()					# 调用主函数
