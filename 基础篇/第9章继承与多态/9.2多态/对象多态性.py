"""
在继承结构中，子类可以根据需要来选择是否要覆写父类中的指定方法，而方法覆写的主要目的在于可以让子类和父类中的方法名称统一，
这样在进行传递时不管子类实例还是父类实例，就都可以使用相同的方法名称进行操作，例如：现在有一个消息发送通道Channel类，
在此类中需要进行消息的发送，而现在的消息分为普通消息，数据库消息，网络消息
"""
# coding : utf-8
class Message: 					# 定义Message父类
    def get_info(self): 				# 定义方法
        return "【Message】www.yootk.com"		# 返回信息
class DatabaseMessage(Message): 			# Message子类
    def get_info(self): 				# 方法覆写
        return "【DatabaseMessage】Yootk数据库信息"	# 返回信息
class NetMessage(Message): 				# Message子类
    def get_info(self): 				# 方法覆写
        return "【NetMessage】Yootk网络信息"		# 返回信息
class Channel: 					# 定义Channel类
    def send(self,msg): 				# 定义方法
        print(msg.get_info())				# 输出内容
def main():					# 主函数
    channel = Channel()  				# 实例化通道类对象
    channel.send(Message())   				# 发送普通消息
    channel.send(DatabaseMessage())  			# 发送数据库消息
    channel.send(NetMessage())    			# 发送网络消息
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
