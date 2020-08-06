"""
本程序实现了UDP客户端操作，在进行客户端访问是，如果可以连接主机，则会触发EchoClient.startProtocol()回调操作
而当客户端接收到服务端响应时则会触发EchoClient。datagramReceived()方法进行数据处理
"""
import twisted  						# pip install twisted
import twisted.internet.protocol 				# 事件处理
import twisted.internet.reactor 				# reactor处理
SERVER_HOST = "127.0.0.1" 					# 连接主机地址
SERVER_PORT = 0 						# 连接端口号
class EchoClient(twisted.internet.protocol.DatagramProtocol): 	# 定义UDP回调
    def startProtocol(self): 				# 连接回调
        self.transport.connect(SERVER_HOST, 8080) 		# 指定对方的地址和端口
        print("服务器连接成功，可以进行数据交互，如果要结束通讯，则请输入空数据。")
        self.send()					# 连接成功后发送数据
    def datagramReceived(self, datagram, addr): 		# 接收数据回调
        print(datagram.decode("UTF-8")) 			# 打印接收到的信息
        self.send()					# 重新输入
    def send(self): 					# 发送数据
        input_data = input("请输入要发送的数据：") 		# 接收键盘数据
        if input_data: 					# 数据不为空则进行发送
            self.transport.write(input_data.encode("UTF-8")) 	# 向服务器发送数据
        else: 						# 输入数据为空
            twisted.internet.reactor.stop()			# 关闭监听
def main():						# 主函数
    twisted.internet.reactor.listenUDP(SERVER_PORT, EchoClient()) # 连接服务器
    twisted.internet.reactor.run()				# 运行程序
if __name__ == "__main__":     				# 判断执行名称
    main()
