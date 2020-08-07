"""
默认状态下，开发者在进行实例化对象输出时，只是返回对象的基本信息以及所占用的内存地址，并不返回一个明确的字符串内容
之所以会出现这样的信息内容，主要是有object类中默认的__str__()方法所决定的，由于默认的__str__()方法只能够获取类名称
以及相关地址信息，这样对于一些有特殊要求的类在功能上就会有所不足，所以开发者可以根据自己需要的显示内容覆写该方法
"""

# coding : utf-8
class Message: 					# 默认object子类
    def __init__(self,content): 			# 构造方法初始化内容
        self.__content = content			# 属性赋值
def main():					# 主函数
    msg = Message("www.yootk.com") 			# 实例化类对象
    print(msg) 					# 直接输出对象
    print(msg.__str__())				# 转为字符串输出
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
