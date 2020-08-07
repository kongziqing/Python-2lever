"""
在进行列表数据操作时，如果要想删除列表的数据，那么就需要__eq__()方法的支持才可以完成
本程序在列表中传入了若干个匿名Member类对象且在使用remove()方法删除数据时，由于__eq__()方法的支持才可以正常实现数据删除操作
"""

# coding : utf-8
class Member(object): 			# object子类
    def __init__(self,name,age): 		# 构造方法
        self.__name = name 			# 实例属性赋值
        self.__age = age			# 实例属性赋值
    def __str__(self): 			# 覆写特殊方法
        return "姓名：%s、年龄：%d" % (self.__name, self.__age)
    def __eq__(self, other): 			# 覆写特殊方法
        if not isinstance(other,Member) or other == None: 	# 判断对象是否合法
            return False 			# 判断失败
        return self.__age == other.__age and self.__name == other.__name
def main():				# 主函数
    member_list = [Member("张三", 18), Member("李四", 20)] 	# 定义人员信息列表
    # 删除数据时传入匿名对象，列表会调用类中“__eq__()”方法
    member_list.remove(Member("张三", 18)) 	# 删除数据
    for mem in member_list: 			# 列表迭代
        print(mem) 				# 输出列表项
if __name__ == "__main__":			# 判断执行名称
    main()					# 调用主函数
