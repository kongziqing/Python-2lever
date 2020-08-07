"""
在子类继承父类的结构中，自乐会继承父类中所有的属性和方法
本程序在定义Parents父类时没有对属性和方法进行封装，所有父类的属性和方法都将被子类所继承，需要注意的是，
在大多数情况下类中的属性往往会被封装，建议在实际项目开发中子类通过方法访问父类属性。
"""
class Parent: 					# 定义父类
    def __init__(self): 				# 构造方法
        self.msg = "www.yootk.com" 			# 属性未封装
    def get_info(self): 				# 方法定义
        return "沐言优拓"				# 返回数据
class Sub(Parent): 					# 子类定义
    def fun(self): 					# 子类函数
        print("【访问父类属性】msg = %s" % (self.msg)) 	# 调用属性
        print("【调用父类方法】%s" % self.get_info())	# 调用方法
def main():					# 主函数
    sub = Sub()					# 实例化子类对象
    sub.fun()					# 调用子类方法
if __name__ == "__main__":				# 判断程序执行名称
    main()
