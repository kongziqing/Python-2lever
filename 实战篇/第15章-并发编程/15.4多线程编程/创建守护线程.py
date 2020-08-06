"""
之前所创建的全部都属于用户线程，所有的用户线程都是进行核心操作的处理，
而守护线程（Daemon）是一种运行在后台的线程服务线程，当用户线程存在时，守护线程也可以同时存在，如果用户线程全部消失，
（程序执行完毕，JVM进程结束），则守护线程也会消失

本程序创建了两个线程，其中一个线程为守护线程，在用户线程未执行完毕前守护线程将持续执行，而当用户线程结束后守护线程也将停止运行。
"""
import threading, time				# 导入线程实现模块
class MyThread(threading.Thread): 			# 线程类
    def __init__(self, thread_name, delay, count): 	# 构造方法
        super().__init__(name=thread_name) 		# 调用父类构造
        self.__delay = delay				# 保存延迟属性
        self.__count = count				# 循环次数
    def run(self): 					# 线程运行方法
        for num in range(self.__count): 			# 依据循环次数执行循环
            time.sleep(self.__delay)  			# 操作延迟
            print("【%s】num = %s" % (
                threading.current_thread().getName(), num)) 	# 输出线程提示信息
def main():					# 主函数
    user_thread = MyThread("用户线程", 2, 5) 		# 实例化线程对象
    daemon_thread = MyThread("守护线程", 1, 999) 		# 实例化线程对象
    daemon_thread.setDaemon(True)  			# 设置守护线程
    user_thread.start()				# 启动用户线程
    daemon_thread.start()				# 启动守护线程
if __name__ == "__main__":				# 判断程序执行名称
    main()
