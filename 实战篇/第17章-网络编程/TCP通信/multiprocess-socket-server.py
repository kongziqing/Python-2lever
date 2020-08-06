#多进程模式处理用户请求
import socket,multiprocessing,os #导入相关组件
SERVER_HOST= "localhost" #监听主机
SERVER_PORT=8080 #监听端口
def echo_handle(client_conn,address):
    print("客户端连接地址：%s、连接端口：%s"%address) #打印提示信息
    with client_conn: #通过客户端连接操作
        while True:#持续进行数据交互
            data=client_conn.recv(100).decode("UTF-8")#接收客户端发送的请求数据
            if data.upper()=="BYEBYE": #信息结束标记
                client_conn.send("exit".encode("UTF-8"))#发送结束标记
                break
            else:
                client_conn.send(("[echo]%s"%data).encode("UTF-8"))
def main():
    with socket.socket() as server_socket:#创建socket对象
        server_socket.bind((SERVER_HOST,SERVER_PORT))#绑定端口
        server_socket.listen()#端口监听
        print("服务器启动完毕，在”%s“端口上监听，等待客户端连接。。。"%SERVER_PORT)
        while True:#持续等待客户端连接
            client_conn, address = server_socket.accept() #客户端连接，进入阻塞状态
            #客户端连接到服务器端时，将启动一个新的进程，同时设置请求处理函数
            process = multiprocessing.Process(target=echo_handle,args=(client_conn,address,),name="客户端进程-%s"%address[1])
            process.start()#进程启动
if __name__=="__main__":
    main()

