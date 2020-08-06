"""
在实际项目中，每一个HTTP服务器都可以同时处理多个用户的请求，所以在自定义HTTP服务器操作过程中
，针对用户的每一次请求一般都需要启动一个新的进程，在每一次请求处理完毕，需要设置响应状态码，头部信息以及响应
内容，下面将实现一个固定HTML数据信息的返回
"""
#定义HTTP服务器
import socket #HTTP服务器基于socket组件开发
import multiprocessing #多进程管理
class HTTPServer:#构造方法
    def __init__(self,port):#构造方法
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #socket.SO_REUSEADDR可以方便地应用绑定在系统核心端口上
        self.server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.server_socket.bind(("0.0.0.0",port))#在当前主机上的指定端口绑定服务
        self.server_socket.listen() #开启监听
    def start(self):#服务器提供服务
        while True:  #持续提供服务
            client_socket,client_address = self.server_socket.accept()#等待客户端连接
            print("[新的客户端连接] 客户IP：%s、访问端口：%s"%client_address)
            # 为每一个客户请求开启一个新的子进程，同时设置不同的进程处理函数
            handle_client_process = multiprocessing.Process(target=self.handle_response,args=(client_socket,))#创建新县城
            handle_client_process.start()#进程启动
            client_socket.close()#进程执行完毕，关闭当前的socket连接
    def handle_response(self,client_socket):#处理用户响应
        request_headers = client_socket.recv(1024)#接收HTTP发送来的数据信息
        print(request_headers.decode()) #获取客户端发送的头部信息
        response_start_line = "HTTP/1.1 200 OK\r\n" #响应状态码
        response_headers = "Server:Yootk Server\r\nContent-Type:text/html\r\n"#响应头部信息
        response_body = "<html>" \
                        "<head>"\
                        "<title>kkkbalala</title>" \
                        "<meta charset = 'UTF-8'/>"\
                        "</head>" \
                        "<body>" \
                        "<h1> lulala</h1>"\
                        "<h1>gugugugugu</h1>" \
                         "</body>"\
                         "</html>" #构造HTML数据
        response = response_start_line+response_headers+"\r\n"+response_body#响应数据
        client_socket.send(bytes(response,"utf-8"))#向客户端返回响应数据
        client_socket.close() #关闭客户端连接
def main():#主函数
    http_server = HTTPServer(80)#创建HTTP服务器并设置监听端口
    http_server.start()#启动HTTP服务器
if __name__ == '__main__':
    main()