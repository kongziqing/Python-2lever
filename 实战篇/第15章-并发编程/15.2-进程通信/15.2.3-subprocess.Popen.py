"""
在subprocess类中提供有一个Popen类，该类的主要功能是可以实现子进程的命令交互，该类构造方法定义如下
def __init__(self,.........)
在该类中定义有多个参数，核心参数的作用如下：：
args:要执行的shell命令，内容可以设置字符串或者列表
bufsize:缓冲区大小
...
...
...
本程序利用Popen类的构造方法在“e：”盘下创建了一个yootk子目录，由于当前的操作系统同为Windows，所以创建
目录的操作使用md命令完成
"""
import subprocess					# 模块导入
def main():					# 主函数
    subprocess.Popen("md yootk", shell=True, cwd="e:/") 	# 创建新的目录
if __name__ == "__main__":				# 判断程序执行名称
    main()
