"""
在进行对象实例化时往往会通过__init__()方法进行相关的初始化操作，而在Python提供的特殊方法里面，还有一个__new__(cls,*args,**kwargs)
方法可以决定是否要调用__init__()实例化对象
在__new__()方法中传入的参数cls就是当前实例化类的信息，同时在此方法中可以返回一个实例化对象，这样才可以继续调用__init__()方法，否则将不会调用

本程序在类中定义了两种构造方法，__new__()方法优先于__init__()方法，如果在__new__()方法中，没有返回object.__new__(cls),
那么对象将无法进行构造，此时msg的内容将为None

提问：使用哪个构造方法？
通过以上实例发现__new__()和__init__()方法都是在构造的时候出现的，那么在开发中使用哪种方法呢？
回答：__new__()主要用于类的整体构造
以工人生产产品为例，实际上__new__()方法像是创建了一个产品加工的工厂（类的整体构造），而__init__()则更像是构造工人(对象构造),
并且在__init__()方法中也提供了参数self引用当前对象，这实际都是由__new__()完成的，所以在开发中经常使用__new__()构造器创建一些公共的类属性处理。
"""
# coding : utf-8
class Message: 					# 默认object子类
    def __new__(cls, *args, **kwargs): 			# 特殊方法
        print("【new】cls = %s、args = %s、kwargs = %s" % (cls,args,kwargs)) 	# 提示信息
        return object.__new__(cls)  			# 如果不返回此内容构造方法将不会执行
    def __init__(self, **kwargs): 			# 构造方法
        print("【init】kwargs = %s" % kwargs) 		# 输出构造方法接收关键字参数
def main():					# 主函数
    msg = Message(title="yootk",content="优拓软件学院")	# 实例化Message类对象
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
