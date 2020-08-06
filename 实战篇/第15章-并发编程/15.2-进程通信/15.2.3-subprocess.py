"""
subprocess模块的主要功能是启动一个新的系统应用进程，同时也可以利用输入输出管道连接这些
子进程，获得子进程的返回内容，在subprocess模块中提供了call()函数，使用该函数可以直接调用
系统命令，call()命令定义如下：
def call(*popenargs,timeout=none,**kwargs)

本程序通过call()函数调用了windows系统中的dir命令，这样就可以在程序中返回当前目录详细列表
"""


import subprocess				# 模块导入
def main():				# 主函数
    subprocess.call("dir /a", shell=True) 	# 执行系统dir命令，shell表示允许直接执行命令
if __name__ == "__main__":			# 判断程序执行名称
    main()
