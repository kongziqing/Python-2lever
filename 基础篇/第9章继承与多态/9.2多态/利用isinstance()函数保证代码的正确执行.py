"""
虽然以上事例实现了一个参数的统一接收，但是，Python语言最大的特点是所有的变量定义时不需要进行类型的定义，所有此时程序中的
Channel.send()方法中的msg参数可以传递非Message类型

当程序中传入了一个字符串对象，但是在字符串对象中并没与get_info()方法，这样程序在执行的过程中就会出现错误，若解决这样的错误，
最方便的做法是追加一个实例的类型判断，可以使用内置的“isinstance(对象，类)”函数，在此函数中需要传递一个对象与要判断的类型，如果该
对象为此类实例，则返回True，否则返回False
"""
class Message: 					# 定义Message父类
    def get_info(self): 				# 定义方法
        return "【Message】www.yootk.com"		# 返回信息
class DatabaseMessage(Message): 			# Message子类
    def get_info(self): 				# 方法覆写
        return "【DatabaseMessage】Yootk数据库信息"	# 返回信息
class NetMessage(Message): 				# Message子类
    def get_info(self): 				# 方法覆写
        return "【NetMessage】Yootk网络信息"		# 返回信息
# class Channel: 					# 定义Channel类
#     def send(self,msg): 				# 定义方法
#         print(msg.get_info())				# 输出内容
# 其它重复代码、略…
class Channel: 					# 定义Channel类
    def send(self,msg): 				# 定义方法
        if isinstance(msg,Message): 			# 判断msg是否属于Message或其子类实例
            print(msg.get_info())			# 调用方法

def main():					# 主函数
    channel = Channel()  				# 实例化通道类对象
    channel.send("小李老师")   				# 发送普通消息

if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
