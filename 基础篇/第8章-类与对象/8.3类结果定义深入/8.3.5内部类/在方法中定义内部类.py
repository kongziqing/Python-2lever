"""
内部类除了可以定义在类中，也可以在方法中进行定义，在方法中定义的内部类可以直接访问方法中的参数或局部变量
本程序在Outer.fun()方法中定义了一个内部类Inner，这样该内部类就可以直接访问fun（）方法中的msg参数与subtitle局部变量
"""
# coding : utf-8
class Outer: 					# 自定义外部类
    def __init__(self): 				# 构造方法
        self.__info = "www.yootk.com" 			# 外部类实例属性
    def print_info(self,title): 			# 信息输出方法
        print("%s：%s" % (title,self.__info)) 		# 信息输出
    def fun(self, msg): 				# 定义方法
        out_obj = self				# 保存外部类实例
        subtitle = "优拓"  				# 方法局部变量
        class Inner: 				# 方法中定义内部类
            def send(self): 				# 内部类方法
                out_obj.print_info(msg + subtitle) 	# 调用外部类实例
        Inner().send()				# 内部类匿名对象调用方法
def main():					# 主函数
    out = Outer()  					# 实例化外部类对象
    out.fun("沐言")					# 调用方法
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
