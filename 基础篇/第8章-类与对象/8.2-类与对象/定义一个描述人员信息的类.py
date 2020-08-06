"""
在本程序的Member类找那个定义了两个方法，set_info(),get_info(),并且在set_info()函数中
定义了name和age两个实例属性，实例属性的内容为方法中参数设置的数据
"""
# coding : utf-8
class Member: 					# 自定义程序类
    """
    定义信息设置方法，该方法需要接收name与age两个参数内容，
    self描述的是当前对象实例，只要是类中的方法都需要加上这个描述
    """
    def set_info(self,name,age): 			# 定义一个信息设置方法
        self.name = name				# 为类中定义实例属性
        self.age = age				# 为类中定义实例属性
    def get_info(self): 				# 方法定义
        """
            获取类中属性内容
        """
        return "姓名：%s，年龄：%d" % (self.name,self.age) 	# 返回对象信息
def main():				# 主函数
    mem = Member()  				# 实例化Member类对象
    mem.set_info("小李老师", 18)  		# 调用set_info()方法并设置相应属性内容
    print(mem.get_info())  			# 获取属性内容
    print("【类外部调用属性】name属性内容：%s、age属性内容：%d"
		% (mem.name, mem.age)) 	# 输出对象信息
if __name__ == "__main__":			# 判断程序执行名称
    main()					# 调用主函数
