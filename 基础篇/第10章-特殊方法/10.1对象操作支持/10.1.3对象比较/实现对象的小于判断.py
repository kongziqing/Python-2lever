"""
对象属于引用数据类型，如果要想比较对象的大小，首先必须保证比较的对象类型相同，其次，还需要对对象的属性依次比较，object类中
默认提供了对象比较的方法，只需要覆写下表中的方法即可实现比较

1.__eq__(self,other)  对象相等比价，other为比较的另一个对象
2.__ne__(self,other)  对象不等比较，other为比较的另一个对象
3.__lt__(self,other)  对象小于比较，other为比较的另一个对象
4.__le__(self,other)  对象小于等于比较，other为比价的另一个对象
5.__gt__(self,other)  对象大于比较，other为比价的另一个对象
6.__ge__(self,other)  对象大于等于比较，other为比价的另一个对象
7.__bool__(self,other)  获取布尔环境内容

本程序在Member类中覆写了__le__()方法，此方法的主要功能是进行属性的"小于等于"判断，本次使用age属性来确定两个实例化对象的大小关系
"""
# coding : utf-8
class Member(object): 				# 默认object子类
    def __init__(self,name,age): 			# 构造方法初始化属性内容
        self.__name = name 				# 实例属性赋值
        self.__age = age 				# 实例属性赋值
    def __le__(self, other): 				# 覆写特殊方法
        if not isinstance(other,Member) or other == None: 	# 判断对象是否合法
            return False    				# 返回False，表示判断失败
        return self.__age <= other.__age  		# 摘选属性判断
def main():					# 主函数
    mem_a = Member("张三", 18) 			# 实例化Member类对象
    mem_b = Member("李四", 20) 			# 实例化Member类对象
    print(mem_a <= mem_b) 				# 大小比较，调用“__le__()”
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
