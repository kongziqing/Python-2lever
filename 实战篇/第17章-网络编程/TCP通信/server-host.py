#导入socket组件
"""
socket() 获取socket类对象
bind((hostname,port)) 在指定主机的端口绑定监听
listen() 在绑定端口上开启监听
accept() 等待客户端连接，连接后返回客户端地址
send(data) 发送数据
recv(buffer) 接收数据
close() 关闭套接字连接
connect((hostname,port)) 设置要连接的主机名称和端口号
"""
import socket
#或者为“127.0.0.1”
SERVER_HOST = "localhost"
#监听端口
SERVER_PORT = 8080
def main():
    #创建socket对象
    with socket.socket() as server_socket:
        #绑定端口
        server_socket.bind((SERVER_HOST,SERVER_PORT))
        #端口监听
        server_socket.listen()
        print("服务器启动完毕，在“%s”端口监听，等待客户端连接。。"%SERVER_PORT)
        #客户端连接，进行入阻塞状态
        client_conn,address = server_socket.accept()
        with client_conn:#通过客户端连接操作
            #返回一个元组
            print("客户端连接地址：%s、连接端口：%s"%address)
            #向客户端发送字节数据
            client_conn.send("kkkk：www.smlie".encode("UTF-8"))
if __name__=="__main__":#判断执行名称
    main()#调用主函数