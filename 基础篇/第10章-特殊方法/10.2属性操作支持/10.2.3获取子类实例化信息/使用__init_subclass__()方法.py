"""
在Python类继承结构之中，当子类定义了构造方法，并且没有通过super().__init__()显式调用父类构造方法时，所有父类是无法知道子类是否
产生了新的实例化对象的，为了解决这样一个问题，Python提供了一个钩子方法
__init_subclass__(cls,**kwargs)
该方法主要定义了在父类，每当其子类对象实例化时，都会自动调用此方法，同时利用此方法可以获得子类的信息以及子类定义类时锁配置的元数据

通过此实例可以发现，在当前子类定义中除了定义了继承的父类之外，还定义了两个类的元数据
子类构造方法并没有强制调用父类指定方法，然后当对象实例化时依然调用了父类的__init_subclass__()方法，并且在此方法中可以获取当前实例化
的子类信息以及子类定义时的元数据
"""

# coding : utf-8
class Parent(object): 					# 定义父类
    def __init__(self): 					# 父类无参构造，此方法不会执行
        print("【Parent】__init__()") 				# 创建目的：方便读者观察
    def __init_subclass__(cls, **kwargs): 			# 覆写特殊方法
        print("【Parent-subclass】cls = %s" % (cls)) 		# 获取子类信息
        print("【Parent-subclass】kwars = %s" % (kwargs)) 		# 获取子类信息
# 定义子类，同时设置子类操作相关的元数据（使用字典的形式进行定义）
class Sub(Parent, url="www.yootk.com", teacher="李兴华"):		# 定义子类
    def __init__(self): 					# 子类构造，不调用父类构造
        print("【Sub】__init__()")				# 输出提示信息
def main():						# 主函数
    sub = Sub()						# 实例化子类对象
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
