"""
因为UDP避免了繁琐的可靠连接步骤，所以其性能要高于基于TCP协议的服务器，在twisted实现了的TCP
程序需要进行连接的操作控制，所以在处理时往往需要一个工厂类负责连接管理，但是UDP的实现方式有所不同，
因为UDP不需要进行连接处理，一个UDP套接字可以接收来自网络上任何一台主机的报文数据，如果想要实现UDP，
只需要继承DatagramProtocol类并覆写相应方法，即可实现事件回调处理

本程序通过twisted实现了一个UDP程序模型，这样在进行时间处理时不再需要处理连接的相关回调操作，只需要对数据的交互进行操作即可
"""
#建立服务器端信息
import twisted  						# pip install twisted
import twisted.internet.protocol 				# 事件处理
import twisted.internet.reactor    				# reactor处理
SERVER_PORT = 8080 					# 监听端口
class EchoServer(twisted.internet.protocol.DatagramProtocol): 	# 继承数据报协议
    def datagramReceived(self, datagram, addr): 		# 接收数据处理
        print("接收到消息，消息来源IP：%s、消息来源端口：%s" % addr) # 信息输出
        print("接收到数据信息：%s" % datagram.decode("UTF-8")) 	# 信息输出
        echo_data = "【ECHO】%s" % datagram.decode("UTF-8") 	# 回应消息
        self.transport.write(echo_data.encode("UTF-8"), addr) 	# 发送消息
def main():						# 主函数
    twisted.internet.reactor.listenUDP(SERVER_PORT, EchoServer()) # 服务监听
    print("服务器启动完毕，等待客户端连接...") 			# 提示信息
    twisted.internet.reactor.run()				# 事件循环
if __name__ == "__main__":     				# 判断执行名称
    main()
