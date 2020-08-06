"""
本程序创建了10个进程，但是由于Lock锁的同步管理，所以这10个进程在进行售票时只允许有一个进程操作，
而其他进程则等待锁资源释放后再抢占操作资源，这样就在锁控制的区域内实现了但进程的执行模式，虽然访问的
数据安全了，但是执行的性能也会有所降低


注意：锁定与释放次数一定要一致，
在使用Lock类进行同步处理时，每调用一次acquire()方法锁定当前操作资源后，一定要调用一次release（）方法释放锁定，
如果此时调用了两次acquire()方法，那么相应的release()方法也要调用两次，否则资源一直被锁定，同时其他进程也无法进行操作
为了解决重复锁定以及资源释放不及时的问题，在multiprocessing模块中提供了一个与Lock对应的Rlock类，此类的最大特点是即便调用
了多次acquire()方法进行锁定，那么只要调用一次release()方法就可以解除锁定，

注意：timeout要大于整个操作延迟时间，同时，注意要在while循环结束后，再加一句release，否则即使程序结束，其他的进程也进不来
"""
import multiprocessing, time						# 模块导入
def work(lock, dict):  						# 售票进程
    while True: 							# 持续卖票
        lock.acquire(timeout=20)   					# 获取锁，超过5秒放弃,也可以不填入时间，但会一直获取锁
        number = dict.get("ticket") 					# 获取字典数据
        if number > 0:  						# 当前还有票
            number -= 1 						# 修改当前票数
            print("【%s】ticket = %s" % (multiprocessing.current_process().name, number))
            time.sleep(0.1)  						# 操作延迟
            dict.update({"ticket":number})				# 更新字典数据
        else: 							# 判断不满足
            break							# 结束循环
        lock.release()           					# 操作完毕释放锁
    lock.release()   #算法改进项，因为最后一次获取了锁，但是没有来得及解锁就已经break了，导致程序结束等待时间过长，因为需要在while循环外再多加一句解锁
def main():							# 主函数
    manager = multiprocessing.Manager()					# 获取Manager对象实例
    lock = multiprocessing.Lock()					# 实例化锁对象
    mgr_dict = manager.dict(ticket=5) 					# 一共卖出5张票
    job_process = [multiprocessing.Process(target=work, args=(lock, mgr_dict,),
      name="售票员 - %s" % item) for item in range(10)] 			# 多个进程共用一个锁
    for process in job_process:  					# 循环进程列表
        process.start()						# 进程启动
    for process in job_process:  					# 循环进程列表
        process.join()						# 进程等待执行完毕
    print("所有进程执行完毕，最终剩余票数：%s" % mgr_dict.get("ticket")) 	# 观察最终剩余票数
if __name__ == "__main__":						# 判断程序执行名称
    main()
