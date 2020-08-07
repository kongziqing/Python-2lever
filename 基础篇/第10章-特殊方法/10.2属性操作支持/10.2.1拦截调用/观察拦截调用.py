"""
在Python中，针对属性的调用与类中方法的执行会提供一个拦截的处理操作方法__getattribute__(),即开发者在使用对象调用类中方法，
或者通过实例化对象获取属性内容前都会通过此方法进行拦截处理，

注意：
实例：触发拦截的操作
调用类中方法  实例化对象.方法()
获取类中属性  print(实例化对象.属性) #实例属性和类属性调用都会触发

实例：不触发拦截的操作
类属性操作   print(类名称.类属性)，类名称.类属性=值
实例对象设置属性内容  实例化对象.属性 =值

通过以上的对比可以发现，只有实例化对象进行类操作时才会有拦截操作
本程序在Message类中覆写了__getattribute__()方法，这样在每次通过实例化对象调用属性和类中方法时都将触发此拦截方法，
但是拦截之后如果要执行完目标操作，那么久必须调用object类中的__getattribute__()方法

本程序在进行拦截处理中，无论是属性还是方法，都使用了统一的处理形式，实际上如果用户有需要，也可以分别对于属性和方法的拦截调用采用不同的方式

"""

# coding : utf-8
class Message: 					# 默认object子类
    def __getattribute__(self, item): 			# 覆写object类方法
        print("【getattribute】item = %s" % (item)) 	# 监听信息提示
        return object.__getattribute__(self, item) 	# 如果不调用此处则代码无法正确执行
    def send(self, info):  				# 定义类中的方法
        print("消息发送：%s" % info) 			# 输出提示信息
def main():					# 主函数
    msg = Message()					# 实例化类对象
    msg.content = "沐言优拓：www.yootk.com"  		# 动态配置实例属性
    print(msg.content) 				# 获取属性触发“__getattribute__()”
    msg.send("www.jixianit.com")  			# 调用方法触发“__getattribute__()”
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
