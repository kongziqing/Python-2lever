"""
defer的最佳用途是在网络通信上，下面将通过一次网络的Echo调用来讲解defer的用法，（使用前twisted实现的TCP服务端已完成）
本程序将采用TCP的方式完成通信，客户端代码如下：
本程序在网络的通信中使用了defer模式，在程序执行中利用time.sleep()模拟了本地操作的延迟，在本地操作完成后才会将处理后的数据交由
handle_success()方法进行处理
"""
import twisted.internet.reactor 				# reactor处理
import twisted.internet.threads 				# defer线程处理
import twisted.internet.defer 				# defer处理
import time 						# 模拟延迟
SERVER_HOST = "localhost" 					# 服务主机
SERVER_PORT = 8080 					# 连接端口
class DeferClient(twisted.internet.protocol.Protocol): 		# 定义客户端监听
    def connectionMade(self): 				# 连接成功时调用
        print("服务器连接成功，可以进行数据交互，如果要结束通讯，则请输入空数据。")
        self.send()  					# 连接成功后发送数据
    def dataReceived(self, data): 				# 数据接收时调用
        content = data.decode("UTF-8") 			# 接收数据解码
        # 在每一次进行数据处理时都启动一个Defer线程，同时设置好相应的回调方法
        twisted.internet.threads.deferToThread(self.handle_request, content).addCallback(self.handle_success) 		# 回调处理
    def handle_request(self, content): 			# 客户端处理
        print("【客户端】对服务器端回应的数据（%s）进行处理，此处产生1秒延迟..." % content)
        time.sleep(1) 					# 客户端操作模拟延迟
        return content 					# 返回处理内容
    def handle_success(self, result): 			# 处理完成
        print("处理完成，进行参数接收：%s" % result) 		# 提示信息
        self.send()						# 继续输入数据
    def send(self): 					# 发送数据
        input_data = input("请输入要发送的数据：") 		# 接收键盘数据
        if input_data: 					# 数据不为空则进行发送
            self.transport.write(input_data.encode("UTF-8")) 	# 向服务器发送数据
        else: 						# 输入数据为空
            self.transport.loseConnection()			# 断开服务器连接
class DefaultClientFactory(twisted.internet.protocol.ClientFactory): # 定义客户端工厂类
    protocol = DeferClient 					# 设置回调程序类
    # 当客户端断开连接或者连接失败时则停止reactor循环监听
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: \
		twisted.internet.reactor.stop()		# 失败结束
def main():						# 主函数
    twisted.internet.reactor.connectTCP(SERVER_HOST,
		SERVER_PORT, DefaultClientFactory())  	# 连接服务器
    twisted.internet.reactor.run()  				# 运行程序
if __name__ == "__main__":     				# 判断执行名称
    main()
