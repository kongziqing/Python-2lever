"""
提问：类方法有什么意义？
通过程序比较发现类方法和静态方法除了在接受参数上有所限制之外并没有其他的区别，那么为什么Python还要提供一个类方法呢？
回答：弥补结构上设计的缺陷
许多的编程语言都会提供一个重载的概念，可以利用此概念为一个类定义多个构造方法，然而在Python中，每一个类只允许使用__init__()定义一个构造方法并且
不允许重载，这样一来在实际开发中就有可能存在构造方法功能有限的问题，所以python为了解决此类问题提供了类方法的定义，可以通过此方法
实现构造方法的重载处理。

本程序原始定义的构造方法中需要接收两个参数，但是假设现在的参数就是一个整体结构--title-url,则此时在构造方法不支持重载的情况下就只能
够利用类方法进行数据处理后再实例化对象，
"""
# coding : UTF-8
class Message: 				# 自定义类
    def __init__(self, title, url): 		# 需要两个参数
        self.__title = title			# 属性设置
        self.__url = url			# 属性设置
    def __str__(self): 			# 对象输出
        return "%s：%s" % (self.__title, self.__url) # 返回属性内容
    @classmethod				# 内置装饰器
    def get_instance(clazz, info): 		# 定义类方法
        result = info.split("-")		# 字符串拆分
        return clazz(result[0], result[1]) 	# 实例化对象
def main():				# 主函数
    msg = Message.get_instance("沐言优拓-www.yootk.com")# 获取实例
    print(msg) 				# 对象打印
if __name__ == "__main__":			# 判断执行名称
    main()					# 调用主函数
