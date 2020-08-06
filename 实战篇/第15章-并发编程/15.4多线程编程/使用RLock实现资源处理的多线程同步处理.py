"""
多线程可以共享程序的资源，所以本程序中创建的10个线程可以共享同一个ticket变量，为了保证售票操作的正确执行，在售票处理sale()函数中
都会进行售票操作的锁定，这样就可以保证只有一个线程执行售票处理，为了避免多次锁定造成的解锁问题，本次使用了RLock类实现同步锁定处理。
"""
import threading, time				# 导入线程实现模块
ticket = 8						# 定义总票数
def sale(lock): 					# 售票操作
    global ticket 					# 使用全局变量
    if lock.acquire():				# 获取锁
        if ticket > 0: 				# 现在有剩余票数
            time.sleep(0) 				# 模拟售票延迟
            ticket -= 1				# 票数减1
            print("【%s】卖票，剩余票数：%s" % (threading.current_thread().name, ticket)) # 信息输出
        lock.release()				# 释放锁
def main():					# 主函数
    lock = threading.RLock()				# 两个业务资源
    thread_list = [threading.Thread(target=sale, args=(lock,), # 创建线程列表
      name="售票员 - %s" % item) for item in range(10)] 	# 创建10个售票线程
    for thread in thread_list: 			# 迭代线程列表
        thread.start()				# 多线程卖票
if __name__ == "__main__":				# 判断程序执行名称
    main()
