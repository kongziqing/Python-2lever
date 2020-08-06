"""
本程序通过twisted实现了一个客户端程序，与服务端的处理形式相同，客户端需要有一个专属的
client类定义所有的回调处理函数，当客户端连接成功后，开始进行数据交互，如果客户端向服务器端输入的
数据为空，则断开连接，停止reactor循环监听，客户端结束通信
"""
import twisted  						# pip install twisted
import twisted.internet.protocol				# 事件处理
import twisted.internet.reactor				# reactor处理
SERVER_HOST = "localhost" 					# 监听地址
SERVER_PORT = 8080 					# 监听端口
class Client(twisted.internet.protocol.Protocol): 		# 定义客户端回调
    def connectionMade(self): 				# 连接触发
        print("服务器连接成功，可以进行数据交互，如果要结束通讯，则请直接回车。")
        self.send()					# 连接成功后发送数据
    def send(self): 					# 发送数据
        input_data = input("请输入要发送的数据：") 		# 接收键盘数据
        if input_data: 					# 数据不为空则进行发送
            self.transport.write(input_data.encode("UTF-8")) 	# 向服务器发送数据
        else: 						# 输入数据为空
            self.transport.loseConnection()			# 断开服务器连接
    def dataReceived(self, data): 				# 接收到服务器端响应
        print(data.decode("UTF-8")) 				# 打印接收到的信息
        self.send()					# 重新输入
class DefaultClientFactory(twisted.internet.protocol.ClientFactory): # 定义客户端工厂类
    protocol = Client 					# 设置回调程序类
    # 当客户端断开连接或者连接失败时则停止reactor循环监听
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: \
		twisted.internet.reactor.stop()
def main():						# 主函数
    twisted.internet.reactor.connectTCP(SERVER_HOST,
		SERVER_PORT, DefaultClientFactory())		# 连接服务器
    twisted.internet.reactor.run()				# 运行程序
if __name__ == "__main__":     				# 判断执行名称
    main()
