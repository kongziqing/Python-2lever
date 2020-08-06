"""
threading实现多线程
threading 是Python提供的新的线程开发模块，除了支持基本的线程处理外，也提供了大量的工具类，本课程使用此模块讲解了多线程的实现以及线程
相关信息的获取

threading是一个最新的多线程实现模块，拥有更加方便的线程控制以及线程同步支持，在此模块中提供了一个Thread类实现线程的相关
处理操作，Thread类的常用方法如表
threading.Thread 类常用方法

def __init__(self,group=None,target=None,name=None,args=(),kwargs=None,*,daemon=None)
        构建一个线程对象，参数作用如下
        group:分组定义
        target：线程处理对象（代替run（）方法）
        name:线程名称，若不设置，则自动分配一个名称
        args：线程处理对象所需要的执行参数
        kwargs:调用对象字典
        daemon:是否设置为后台线程
def start(self)  线程启动
def run(self)   线程操作主题，若没设置target处理函数，则执行此方法
def join(self,timeout=None)  线程强制执行
def name(self)  获取线程名称
def ident(self)  获取线程标识
def is_alive(self)  判断线程存活状态

使用threading.Thread实现的多线程可以设置线程的执行函数，也可以定义单独的线程处理类，由于
多线程的运行状态不确定，所以可以利用threading.current_thread()函数动态获取当前正在执行方法体的
线程对象
"""


import threading, time				# 导入线程实现模块
def thread_handle(delay): 				# 线程处理函数
    for num in range(5): 				# 迭代操作
        time.sleep(delay) 				# 操作延迟
        print("【%s】num = %s" % (
            threading.current_thread().getName(), num)) 	# 输出线程提示信息
def main():					# 主函数
    for item in range(10): 				# 迭代操作
        thread = threading.Thread(target=thread_handle, args=(1,), name="执行线程 - %s" % item)
        thread.start()				# 启动子线程
if __name__ == "__main__":				# 判断程序执行名称
    main()
