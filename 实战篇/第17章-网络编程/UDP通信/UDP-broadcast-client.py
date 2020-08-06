"""
UDP广播接收端
如果要想实现UDP广播的处理操作，则需要为实例化的Socket类对象设置相关的UDP属性，此时可以使用setsockopt()方法完成
此方法定义如下：
setsockopt(self,level:int,optname:int,value:Union[int,bytes])
该方法主要包含有三个参数
level：设置选项所在的协议层编号，有一下四个可用的配置项
*socket.SOL_SOCKET:基本套接字接口
*socket.IPPROTO_IP:IPv4套接字接口
*socket.IPPROTO_IPv6:IPv6套接字接口
*socket.IPPROTO_TCP:TCP套接字接口
optname:设置选型名称，例如，如果要进行广播，则可以使用socket.BROADCAST.
value：设置选项的具体内容
"""
import socket
BROADCAST_CLIENT_ADDR  = ("0.0.0.0",21567)#客户端绑定地址
def main():
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as client_socket:#创建广播socket
        client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1) #设置广播模式
        client_socket.bind(BROADCAST_CLIENT_ADDR) #绑定监听地址
        while True:
            message,address = client_socket.recvfrom(100) #接收广播消息
            print("消息内容：%s、消息来源IP：%s、消息来源端口：%s"%(message.decode("UTF-8"),address[0],address[1]))#打印消息来源
if __name__ == '__main__':
    main()

