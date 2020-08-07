"""
本程序在Message类中覆写了__str__()方法，这样就可以由开发者自行定义对象输出的信息内容
"""
# coding : utf-8
class Message: 					# 默认object子类
    def __init__(self,content): 			# 构造方法初始化内容
        self.__content = content			# 属性初始化
    def __str__(self): 				# 覆写object类方法
        return "【__str__()】%s" % self.__content		# 获取对象信息
def main():					# 主函数
    msg = Message("www.yootk.com")			# 实例化类对象
    print(msg) 					# 直接输出对象
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
