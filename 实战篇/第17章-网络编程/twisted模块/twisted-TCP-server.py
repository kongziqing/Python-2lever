"""
twisted简化了多线程模型的切换以及性能损耗问题，基于异步实现服务器处理，
本课程通过具体的代码以及运行操作实现了新的Echo服务器端与客户端的开发

使用twisted模块最大的特点是优化服务器端的处理资源，下面将使用twisted实现了一个TCP的Echo
程序模型，在本模型中首先针对数据交互定义专属的处理协议类，在该类中定义所有的回调处理时间，而如果要想
将此协议类在Reactor中注册，还需要提供一个Factory工厂类，该类的主要功能是进行客户端的连接管理，服务器端程序
的实现结构如图17-21所示


本程序实现了一个TCP服务器端，在本程序开发中并没有进行任何有关多进程与多线程的处理，所有的程序都是在单线程环境下运行，每当有新的客户端连接之后，reactor会监听
到此事件，随后触发Server.connectionMade()方法，当客户端发送数据给服务端是该事件也会被reactor监听到，并且调用Server。dataReceived（）方法进行请求回应
"""
#编写服务端程序
import twisted  						# pip install twisted
import twisted.internet.protocol 				# 事件处理
import twisted.internet.reactor 				# reactor处理
SERVER_PORT = 8080 					# 监听端口
class Server(twisted.internet.protocol.Protocol): 		# 定义回调处理类
    def connectionMade(self): 				# 客户端连接时触发
        print("客户端地址：%s" % self.transport.getPeer().host) 	# 提示信息
    def dataReceived(self, data): 				# 客户端发送数据时触发
        print("【服务器】接收到数据：%s" % data.decode("UTF-8"))	# 提示信息
        self.transport.write(("【ECHO】%s" %
	data.decode("UTF-8")).encode("UTF-8")) 		# 向客户端回应信息
class DefaultServerFactory(twisted.internet.protocol.Factory): 	# 定义工厂类
    protocol = Server 					# 注册事件回调处理类
def main():
    twisted.internet.reactor.listenTCP(SERVER_PORT, DefaultServerFactory()) # 服务监听
    print("服务器启动完毕，等待客户端连接...") 			# 提示信息
    twisted.internet.reactor.run()				# 事件循环
if __name__ == "__main__":     				# 判断执行名称
    main()
