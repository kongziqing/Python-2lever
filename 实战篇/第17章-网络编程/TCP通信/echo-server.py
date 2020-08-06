"""
Echo是一个在操作系统中较为常见的命令，该命令的主要特点是可以直接将给定的数据进行回显，
在网络编程中可以利用Echo的操作命令形式实现数据交互的处理操作，即客户端通过键盘输入数据，
随后将此数据发送到服务器端，服务器端接收到数据后再数据前面追加【ECHO】的前缀标记后将数据返回给客户端

本程序实现了一个循环接收客户端数据的服务端程序，每当客户端发送数据后会在数据前追加【ECHO】标记信息后返回，
如果客户端发出的是一个结束命令，则会退出循环，同时向客户端发送一个exit的结束命令
"""
import socket #导入相关组件
SERVER_HOST = "localhost" #或者为127.0.0.1
SERVER_PORT = 8080 #监听端口
def main():
    with socket.socket() as server_socket:
        server_socket.bind((SERVER_HOST,SERVER_PORT))#绑定端口
        server_socket.listen()#端口监听
        print("服务器启动完毕，在”%s“端口上监听，等待客户端连接。。。"%SERVER_PORT)
        client_conn,address = server_socket.accept()#客户端连接，进入阻塞状态
        with client_conn:#通过客户端连接操作
            print("客户端连接地址：%s、连接端口：%s"%address)#返回一个元组
            while True:#持续进行数据交互
                data=client_conn.recv(100).decode("UTF-8")#接收客户端发送的请求数据
                if data.upper()=="BYEBYE":
                    client_conn.send("exit".encode("UTF-8"))
                    break
                else:
                    client_conn.send(("kongziqing_%s"%data).encode("UTF-8"))#回应数据
if __name__ == "__main__":
    main()


