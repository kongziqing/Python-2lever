"""
向进程写入数据
本程序通过subprocess模块启动了一个Python命令子进程，并且利用stdin向子进程输入了若干命令语句，而子
进程中的执行结果可以通过stdout获取，子进程的错误信息可以通过stderr获取
"""
import subprocess							# 模块导入
def main():							# 主函数
    open_process = subprocess.Popen("python.exe", stdin=subprocess.PIPE,
	stdout=subprocess.PIPE, stderr=subprocess.PIPE) 			# 创建子进程
    # 通过stdin向subprocess子进程发送执行命令，数据必须使用encode()编码、decode()解码
    open_process.stdin.write("print('沐言优拓：www.yootk.com')\n".encode())	# 【正确】输出提示信息
    open_process.stdin.write("name = '李兴华'\n".encode())			# 【正确】声明变量
    open_process.stdin.write("print('课程讲师：%s' % name)\n".encode())		# 【正确】格式化输出
    open_process.stdin.write("print(10 + 20)\n".encode())			# 【正确】数学计算
    open_process.stdin.write("'No.' + 1".encode())				# 【错误】类型不匹配
    open_process.stdin.close()						# 关闭进程输入
    # 通过stdout获取subprocess子进程执行后的提示信息
    cmd_out = open_process.stdout.read()					# 获取进程输出内容
    open_process.stdout.close()  					# 关闭进程输出
    print(cmd_out.decode())						# 输出进程返回结果
    cmd_error = open_process.stderr.read()				# 获取进程错误信息
    open_process.stderr.close()   					# 关闭进程输出
    print(cmd_error.decode())						# 获取进程错误信息
if __name__ == "__main__":						# 判断程序执行名称
    main()
