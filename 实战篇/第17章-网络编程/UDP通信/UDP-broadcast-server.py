import socket
BROADCAST_SERVER_ADDR = ("<broadcast>",21567) #广播地址
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:#服务器端Socket
        server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1) #设置广播模式
        a=1
        while(True):
            if a==100:
                break
            else:
                server_socket.sendto("吧啦啦啦".encode("UTF-8"),BROADCAST_SERVER_ADDR) #数据发送
                a+=1
if __name__ == '__main__':
    main()