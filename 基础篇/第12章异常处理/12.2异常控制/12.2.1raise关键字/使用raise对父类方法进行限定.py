"""
使用raise控制方法覆写

在很多语言中都会提供有接口的概念，接口的主要作用是规定所有子类必须遵循的方法标准，但是Python为了降低开发的复杂性，并未提供有
接口概念，所以这时就可以利用raise关键字在需要覆写的方法上进行一些限定

本程序在Connect类中定义的build()方法内部使用raise抛出了一个异常，如果开发者直接调用父类的build()方法，就会出现
NotImplementedError异常，而只有在子类中正确覆写此方法后才可以正常调用，这样就对子类方法的覆写进行了约定
"""
# coding : UTF-8
class Connect: 				# 定义父类
    def build(self): 			# 父类不提供此方法实现
        raise NotImplementedError("【Connect】build()方法未实现。")	# 手工抛出异常
class ServerConnect(Connect): 			# 定义子类
    def build(self): 			# 方法覆写
        print("【ServerConnect】连接网络服务器...") # 提示信息
def main():				# 主函数
    conn = ServerConnect()			# 实例化对象
    conn.build()				# 调用被覆写过方法
if __name__ == "__main__":			# 判断程序执行名称
    main()					# 调用主函数
