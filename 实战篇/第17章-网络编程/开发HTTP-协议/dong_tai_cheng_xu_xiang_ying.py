"""
动态请求处理
动态处理是现代web开发的主流模式，本课程利用Python中动态模块导入特点实现相应的动态处理操作，
从而模拟动态执行环境，即根据用户请求实现不同响应内容的处理
本程序在pages包中定义了一个可以被动态加载的echo.py模块，同时内部提供有一个自定义的service()函数，
对于此模块中的函数调用，可以直接通过路径的形式进行指定，例如：/echo/service路径中的echo为模块名称，service为函数名称，
HTTP的动态调用原理如图17-16所示。
"""
import socket, re, multiprocessing, os, sys		# 模块导入
HTML_ROOT_DIR = os.getcwd() + os.sep + "html"  	# 设置HTML静态文件保存目录
sys.path.append("pages") 				# 设置模块加载路径
class HTTPServer: 					# HTTP服务处理类
    def __init__(self, port): 			# 构造方法
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.SO_REUSEADDR可以方便的将应用绑定在系统核心端口上
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("0.0.0.0", port)) 	# 在当前主机的指定端口绑定服务
        self.server_socket.listen()			# 开启监听
    def start(self): 				# 服务器提供服务
        while True: 				# 持续监听用户请求
            client_socket, client_address = self.server_socket.accept() # 等待客户端连接
            print("【新的客户端连接】客户IP：%s、访问端口：%s" % client_address)
            # 为每一个客户请求开启一个新的子进程，同时设置不同的进程处理函数
            handle_client_process = multiprocessing.Process(target=self.handle_response,
			args=(client_socket,)) 	# 创建进程
            handle_client_process.start()		# 进程启动
            client_socket.close()			# 进程执行完毕后，关闭当前的Socket连接
    def handle_response(self, client_socket): 		# 处理用户响应
        request_headers = client_socket.recv(1024) 	# 接收HTTP发送来的数据信息
        # 利用正则进行拆分，通过客户端发送的头信息获取客户端要访问的地址以及参数信息
        file_name = re.match(r"\w+ +(/[^ ]*) ",
		request_headers.decode().split("\r\n")[0]).group(1)
        if file_name.startswith("/pages"): 		# 以“/pages”路径开头的路径为动态路径
            request_name = file_name[file_name.index("/", 1) + 1 : ] # 获取请求模块与函数名称
            param_value = "" 			# 保存传递的参数名称
            if request_name.__contains__("?"): 		# 如果有传递参数
                request_param = request_name[request_name.index("?") + 1 : ] # 获取参数字符串
                param_value = request_param.split("=")[1] # 获取参数内容
                request_name = request_name[0 : request_name.index("?")] # 获取模块与函数名称
            model_name = request_name.split("/")[0] 	# 获取模块名称
            method_name = request_name.split("/")[1] 	# 获取处理函数名称
            model = __import__(model_name) 		# 加载模块
            method = getattr(model, method_name) 	# 加载模块中的函数
            response_body = method(param_value) 	# 处理模块响应
            response_start_line = "HTTP/1.1 200 OK\r\n"  # 响应状态码
            response_headers = "Server: Yootk Server\r\nContent-Type: text/html\r\n"  # 头信息
            reponse = response_start_line + response_headers + "\r\n" + response_body # 回应信息
            client_socket.send(bytes(reponse, "UTF-8"))  # 响应数据
        client_socket.close()  			# 关闭客户端连接
def main():					# 主函数
    http_server = HTTPServer(80) 			# 创建HTTP服务器并设置监听端口
    http_server.start()				# 启动HTTP服务器
if __name__ == "__main__":     			# 判断执行名称
    main()
