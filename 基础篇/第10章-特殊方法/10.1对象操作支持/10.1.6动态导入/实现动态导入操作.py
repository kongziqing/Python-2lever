"""
Python中使用其他模块之前都需要通过import语法采用硬编码的形式进行模块导入，为了更加方便程序的执行，Python提供了一个__import__()
动态导入函数，此函数接收的是一个要导入模块名称的字符串数据，模块导入后就可以利用内置的getattr()函数动态获取模块中的结构进行操作。

本实例先在util.py模块中定义了一个get_info()函数以及一个Message类，接下来将通过动态导入的形式进行加载，如一下实例所示
本程序通过__import__('util')函数动态导入了util模块，这样就可以通过getattr()函数并结合此模块对象动态获取模块中的结构进行调用

"""
# coding : UTF-8
def main():					# 主函数
    util = __import__('util') 				# 导入util.py模块
    get_info_obj = getattr(util, "get_info") 		# 获取模块中的函数引用
    print(get_info_obj())				# 通过引用对象直接调用函数
    message_class = getattr(util, "Message") 		# 获取模块中的类引用
    print(message_class().echo("www.yootk.com"))		# 实例化类对象并调用类中方法
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
