"""
一个方便的HTTP服务器是不可能让用户直接将响应的代码放置在程序中的，而是设置一个专属的工作目录，将需要的HTML文件编辑完成后保存在目录里
在用户发送请求时可以根据用户访问地址加载所需要的的文件内容再进行响应，响应目录如图17-15所示，本节将
采用文件IO流的形式实现响应目录的创建
"""
import socket, re, multiprocessing, os		# 模块导入
HTML_ROOT_DIR = os.getcwd() + os.sep + "html"  	# 设置HTML静态文件保存目录
class HTTPServer: 					# 定义HTTP服务类
    def __init__(self, port): 			# 设置监听端口
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.SO_REUSEADDR可以方便的将应用绑定在系统核心端口上
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("0.0.0.0", port)) 	# 在当前主机的指定端口绑定服务
        self.server_socket.listen()			# 开启监听
    def start(self): 				# 启动服务监听
        while True: 				# 持续监听用户请求
            client_socket, client_address = self.server_socket.accept() # 等待客户端连接
            print("【新的客户端连接】客户IP：%s、访问端口：%s" % client_address)
            # 为每一个客户请求开启一个新的子进程，同时设置不同的进程处理函数
            handle_client_process = multiprocessing.Process(target=self.handle_response,
		                             args=(client_socket,)) 		# 构造进程
            handle_client_process.start()		# 进程启动
            client_socket.close()			# 进程执行完毕后，关闭当前的Socket连接
    def handle_response(self, client_socket): 		# 处理用户响应
        request_headers = client_socket.recv(1024) 	# 接收HTTP发送来的数据信息
        # 利用正则进行拆分，通过客户端发送的头信息获取客户端要访问的文件名称
        file_name = re.match(r"\w+ +(/[^ ]*) ",
		request_headers.decode().split("\r\n")[0]).group(1)
        if "/" == file_name: 			# 访问的是根路径
            file_name = "/index.html"  # 定义真实文件名称
        if file_name.endswith(".html") or file_name.endswith(".htm"):
            client_socket.send(bytes(self.get_html_data(
		file_name), "UTF-8")) 		# 文本响应数据
        else: 					# 二进制响应数据
            client_socket.send(self.get_binary_data(file_name)) # 响应二进制数据
        client_socket.close()   			# 关闭客户端连接
    def read_file(self, file_name): 			# 根据文件名称加载数据
        file_path = os.path.normpath(HTML_ROOT_DIR + file_name)
        file = open(file_path, "rb")			# 二进制读取模式
        file_data = file.read()			# 读取文件内容
        file.close()				# 关闭文件流
        return file_data 				# 返回二进制数据
    def get_binary_data(self, file_name): 		# 加载二进制文件
        response_body = self.read_file(file_name)  	# 加载文件内容
        return response_body 			# 返回文件数据
    def get_html_data(self, file_name): 		# 通过给定的路径进行数据加载
        response_start_line = "HTTP/1.1 200 OK\r\n"  	# 响应状态码
        response_headers = "Server: Yootk Server\r\nContent-Type: text/html\r\n"  # 响应头信息
        response_body = self.read_file(file_name).decode("UTF-8")  # 响应数据信息
        response = response_start_line + response_headers + \
		"\r\n" + response_body  		# 定义响应数据
        return response				# 返回响应数据
def main():					# 主函数
    http_server = HTTPServer(80) 			# 创建HTTP服务器并设置监听端口
    http_server.start()				# 启动HTTP服务器
if __name__ == "__main__":     			# 判断执行名称
    main()
