"""
本程序在Member类中直接覆写了__bool__()方法，这样就可以直接改独享进行布尔逻辑判断
"""
# coding : utf-8
class Member(object): 			# object子类
    def __init__(self,name,age): 		# 构造方法
        self.__name = name 			# 实例属性赋值
        self.__age = age 			# 实例属性赋值
    def __bool__(self): 			# 覆写特殊方法
        return self.__age > 18			# 判断是否成年
def main():				# 主函数
    mem = Member("李四", 20) 			# 实例化Member对象
    if mem: 				# 直接调用“__bool__()”方法返回结果
        print("成年了！")			# 提示信息
if __name__ == "__main__":			# 判断程序执行名称
    main()					# 调用主函数
