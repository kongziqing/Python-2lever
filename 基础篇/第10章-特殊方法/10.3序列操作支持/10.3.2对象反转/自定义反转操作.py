"""
在序列操作对象中可以使用reverse()函数实现存储内容的反转，而对于自定义类的对象也可以进行反转，此时就需要在类中定义__reversed__()特殊方法来完成
本程序在Message类中定义了__reversed__()方法，这样在程序定义时就可以利用reversed()函数直接进行对象反转处理
"""
# coding : utf-8
class Message: 					# 自定义Message类
    def __init__(self): 				# 构造方法
        self.__msg_list = ["沐言优拓","www.yootk.com"]	# 初始化列表
    def get_msg_list(self): 				# 获取属性
        return self.__msg_list				# 返回列表属性
    def __reversed__(self): 				# 对象反转支持
        self.__msg_list = reversed(self.__msg_list) 	# 反转处理
def main():					# 主函数
    msg = Message()					# 实例化类对象
    reversed(msg) 					# 序列反转
    for item in msg.get_msg_list():			# 迭代输出
        print(item, end="、")				# 输出列表项
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
