"""
属性封装之后在类的外部无法通过"对象.属性"的形式进行访问，但这并不意味着在类的内部无法通过此格式进行访问，
下面通过一个特别的代码加以说明
实例：内部通过对象引用修改封装属性
本程序在member类的内部定义了一个inner_change()方法，并且在此方法中传递了一个本类对象的引用，由于是在类的内部，
所以可以直接使用"对象.属性"的形式访问类中定义的封装属性
"""
class Member: 				# 自定义Member类
    def set_name(self, name): 			# 设置name属性内容
        self.__name = name			# 为封装属性name赋值
    def get_name(self): 			# 获取name属性内容
        return self.__name			# 返回封装属性内容
    def inner_change(self,temp): 		# 接收对象引用
        temp.__name = "Yootk" 			# 对象直接访问私有属性
def main():				# 主函数
    mem = Member()				# 实例化Member类对象
    mem.set_name("小李老师")			# 通过setter方法间接访问name属性
    mem.inner_change(mem) 			# 引用传递到内部实现私有属性直接访问
    print(mem.get_name())			# 输出name属性
if __name__ == "__main__":			# 判断程序执行名称
    main()
