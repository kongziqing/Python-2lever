"""
进程间的共享资源可能是一个，也有可能是多个，为了保证有限的共享资源可以被所有的操作进程在操作的同时保持数据的同步，
Python提供了信号量的概率

在大多数情况下，服务器能提供的资源是有限的，
信号量可以通过multiprocessing模块中的Semaphore类实现，该类的操作方法与Lock类似，Semaphore类本质上一种带有计数功能的进程同步机制
（acquire()方法为减少计数，release()方法为增加计数，）当可用信号量的计数为0时，则意味着后续进程将被阻塞，

注意：关于多次释放的问题
在调用Semaphore类中的release()方法释放锁定资源时，如果调用次数不当，则有可能造成可用的信号量范围会超过既定范围，
为了解决这一问题，在multiprocessing模块中又提供了一个BoundedSemaphore类，该类最大的特点是在使用release()方法
释放锁定资源时会查看计数是否超过上限，这样就保证了正确的可用的信号量个数不超过限定范围

本程序创建了3个信号量，这样在程序进行并发处理时，只允许3个进程同时操作，而未获得操作的资格的其他进程则需要等待在线进程释放资源再进行调度
"""
import multiprocessing, time					# 模块导入
def work(sema):  						# 售票进程
    if sema.acquire():					# 等待获取信号量
        print("【%s】进程开始进行业务处理..." % multiprocessing.current_process().name) # 提示信息
        time.sleep(2) 					# 延迟
        sema.release()					# 释放锁
def main():						# 主函数
    sema = multiprocessing.Semaphore(3) 				# 设置3个信号量
    job_process = [multiprocessing.Process(target=work, args=(sema,),
      name="业务客户 - %s" % item) for item in range(10)] 		# 多个进程共用一个信号量对象
    for process in job_process: 				# 循环进程列表
        process.start()					# 进程启动
    for process in job_process: 				# 循环进程列表
        process.join()					# 进程等待执行完毕
if __name__ == "__main__":					# 判断程序执行名称
    main()
