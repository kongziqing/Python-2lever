"""
多继承可以同时获取多个已经存在类的支持，实现更加复杂的继承结构，
本程序实现了一个信息发送操作的功能，NetMessage子类继承了Message与Connect两个父类，随后利用两个父类中提供的方法实现了消息发送
处理业务
在子类没有定义任何构造方法的情况下，Python子类对象实例化时会自动调用父类中的构造方法，但是在多继承结构中，由于一个子类存在有多个父类
，就会造成结构调用的二义性，为了解决这个问题，Python专门提供了一个MRO（Method Resolution Order，方法解析顺序）算法，执行时按照从
左到右的原则进行调用
"""
# coding : utf-8
class Message: 					# 定义Message类
    def send(self,msg): 				# 消息发送
        print("【Message】消息发送：%s" % (msg)) 		# 输出提示信息
class Connect: 					# 定义Connect类
    def build(self): 				# 通道连接
        print("【Connect】连接服务器，创建发送连接...") 	# 输出提示信息
        return True 					# 返回连接结果
    def close(self): 				# 通道关闭
        print("【Connect】服务处理完毕， 关闭服务器连接...") # 输出提示信息
class NetMessage(Message,Connect): 			# 定义消息发送子类
    def net_message(self, msg): 			# 通道测试
        if self.build():				# 调用父类方法
            self.send(msg) 				# 调用父类方法
            self.close()				# 调用父类方法
        else: 					# 连接建立失败
            print("【Error】服务器连接失败，消息无法发送！")	# 输出提示信息
def main():					# 主函数
    net = NetMessage()				# 实例化子类对象
    net.net_message("www.yootk.com") 			# 调用子类方法
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
