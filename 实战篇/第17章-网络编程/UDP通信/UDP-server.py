import socket
SERVER_HOST = "localhost"
SERVER_PORT =  8080
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:#创建UDP服务
        server_socket.bind((SERVER_HOST,SERVER_PORT)) #绑定端口
        print("服务器启动完毕，在”%s“端口上监听，等待客户端连接..."%SERVER_PORT)#提示信息
        while True:#服务器端持续提供服务
            data,addr = server_socket.recvfrom(30)#接收客户端发送的信息
            echo_data = ("【ech0】%s"%data.decode("UTF-8")).encode("UTF-8")#回应信息
            server_socket.sendto(echo_data,addr)#数据发送
            server_socket.sendto(echo_data, addr) #数据发送
if __name__ == '__main__':
    main()