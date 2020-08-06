#用以测试多进程通信
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