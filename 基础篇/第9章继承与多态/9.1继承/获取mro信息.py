"""
在Python中，所有的方法执行顺序信息都会自动保存在一个拓扑序列中，开发者如果想要获得此信息，内容可以使用"类名称.mro()"函数完成
通过执行结果可以发现，如果此时Sub类没有构造方法，则会调用ParentA类中的无参构造方法，如果ParentA类没有构造方法，则会调用Base类中的无参构造方法
"""
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
def main():			# 主函数
    print(Sub.mro())			# 获取mro信息
if __name__ == "__main__":
    main()
