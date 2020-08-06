"""
一个进程中的多个线程可以直接访问共享的资源，为了保证操作的正确性，在进行共享资源操作时就是需要
进行同步处理，在threading类中定义了相应的同步处理类，Event（同步时间）、Semaphore&BoundedSemaphore(信号量)
Barrier（栅栏）、Lock&RLoc(锁)，这些线程同步类的操作与多进程的同步处理操作流程类似。
本程序创建了10个线程对象，随后利用Semaphore控制了可以同时操作的资源数量，在进行操作中会使用acquire()方法尝试获取可用资源，
如果资源已经被占满，则等待其他线程使用release()方法释放资源后才可以继续操作。
"""
import threading, time				# 导入线程实现模块
def bank_handle(semaphore): 				# 线程处理函数
    if semaphore.acquire():				# 获取资源
        print("【%s】资源抢占成功，开始办理个人相关业务 ..." %
	 	 (threading.current_thread().name)) 	# 输出提示信息
        time.sleep(2) 				# 模拟业务办理延迟时间
        semaphore.release()				# 释放资源
def main():					# 主函数
    semaphore = threading.Semaphore(2) 			# 两个业务资源
    thread_list = [threading.Thread(target=bank_handle, args=(semaphore,),
      name="银行客户 - %s" % item) for item in range(10)] 	# 创建10个线程
    for thread in thread_list: 			# 迭代线程列表
        thread.start()				# 多人同时涌进银行开始办理业务
if __name__ == "__main__":				# 判断程序执行名称
    main()
