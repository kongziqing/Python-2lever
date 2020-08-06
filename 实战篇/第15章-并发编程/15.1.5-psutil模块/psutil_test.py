"""
操作系统往往会提供进程管理、磁盘监控的工具，利用这些工具可以帮助人员进行系统维护，Python提供了跨平台支持的
psutil模块，本程序将使用此模块获取进程信息，磁盘信息，以及CPU信息

Python提供了一个psutil(Process and System Utilities,进程和系统工具)的第三方模块，
在psutil模块里面提供有process_iter()方法，该方法会返回一个生成器对象，用户可以直接进行迭代以获取每一个进程的
详细内容

提示：进程列表
当用户使用psutil模块时，可以直接利用模块中提供的test（）实现一个与Linux中ps命令类似的处理效果。
使用test（）方法输出了在交互式环境下的进程信息列表
import psutil
pstuil.test()

"""

import psutil   #psutil 需要单独安装
def main():
    for process in psutil.process_iter():#生成器操作
        print("进程编号：%d、进程名称：%s、创建时间：%s"%(process.pid, process.name(),process.create_time()))#输出进程信息
if __name__ == '__main__':
    main()