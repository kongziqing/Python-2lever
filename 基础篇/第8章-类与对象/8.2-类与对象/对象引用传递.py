"""
类属于Python中的引用数据类型，所以有类所产生的对象也可以进行引用传递处理，引用传递时对
象所传递的是其所对应的内存地址

本程序为了观察对象引用传递的操作效果，特别定义了一个change_member_info()函数，
利用此函数接收一个对象并进行内容修改
"""
class Member: 					# 自定义Member类
    def get_info(self): 				# 定义方法
        return "姓名：%s，年龄：%d" % (self.name,self.age) 	# 返回对象信息
def change_member_info(temp): 				# 定义函数
    """
    定义一个修改函数，该函数的主要功能是修改指定对象中的类属性内容
    :param temp: 要修改的对象引用
    :return: NoneType
    """
    temp.name = "李兴华"       			# 修改实例属性定义
    temp.age = 22   					# 修改实例属性定义
def main():					# 主函数
    mem = Member()   				# 实例化Member类对象
    mem.name = "小李老师"  				# 实例属性定义与赋值
    mem.age = 18   					# 实例属性定义与赋值
    change_member_info(mem) 				# 引用传递
    print(mem.get_info())				# 输出属性内容
if __name__ == "__main__":				# 判断程序执行名称
    main()
