"""
为了方便进行多线程的操作管理，可以将多线程的执行操作封装在一个线程处理类中，此线程类要求继承
Thread类，同时要讲线程的执行操作定义在run（）方法中。

本程序创建了一个MyThread线程类，该类必须继承threading.Thread父类，同时需要复写run（）方法（定义线程执行主体），
当在主函数中创建MyThread子类实例时，就可以通过继承的start()方法启动多线程。


"""
import threading, time				# 导入线程实现模块
class MyThread(threading.Thread): 			# 线程执行类
    def __init__(self, thread_name, delay): 		# 构造方法
        super().__init__(name=thread_name) 		# 调用父类构造
        self.__delay = delay 				# 保存延迟属性
    def run(self): 					# 线程执行函数
        for num in range(5): 				# 线程迭代执行
            time.sleep(self.__delay)  			# 操作延迟
            print("【%s】num = %s" % (
                threading.current_thread().getName(), num)) 	# 输出线程提示信息
def main():					# 主函数
    for item in range(10): 				# 迭代创建线程
        thread = MyThread("执行线程 - %s" % item, 1) 	# 实例化线程类对象
        thread.start()				# 启动子线程
if __name__ == "__main__":				# 判断程序执行名称
    main()
