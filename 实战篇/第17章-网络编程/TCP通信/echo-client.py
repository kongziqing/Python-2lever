"""
本程序实现了一个Echo程序的客户端，由于程序需要进行多次的数据交互，所以设置了一个while循环，
每次循环时用户都通过键盘输入要发送的数据，并将该数据发送到服务器端处理后返回，当服务器端返回数据为exit是，
客户端将结束交互操作并断开与服务器端的连接
此时实现的Echo模型是基于单进程机制实现的网络通信，这样会造成一个问题，在同一段时间之内只允许一个客户端
连接到服务器端进行通信处理，并且当此客户端退出之后服务器端也将随之关闭，为了提升服务器端的处理性能，可以利用多进程
机制来处理多个客户端的通信需求
"""
import socket
SERVER_HOST = "localhost" #连接主机名
SERVER_PORT = 8080 #连接端口
def main():   #主函数
    with socket.socket() as client_socket:     #创建socket对象
        client_socket.connect((SERVER_HOST, SERVER_PORT)) #连接服务器端
        while True:
            input_data = input("请出入要发送的数据：") #键盘数据输入
            client_socket.send(input_data.encode("UTF-8"))  #向服务器端发送数据
            echo_data = client_socket.recv(100).decode("UTF-8")   #接收回应数据
            if echo_data.upper() == "EXIT":
                break
            print(echo_data)
if __name__ == "__main__":
    main()