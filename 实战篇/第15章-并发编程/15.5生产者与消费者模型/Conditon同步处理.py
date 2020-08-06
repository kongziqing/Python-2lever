"""
线程同步问题的关键是进行线程等待与唤醒机制，在threading模块中提供了Condition处理类，这类提供
有锁的处理支持，
在生产者与消费者中，为了实现两个操作线程的同步处理，则需要进行等待与唤醒的同步操作，
当生产者未执行完毕，消费者应该等待生产者执行完毕后才可以消费数据，同理，在消费者未消费完数据后，生产者也应该进行等待，
当各自的线程操作完毕，则应该唤醒其他等待线程以继续执行后续操作，

threading.Conditon类的常用操作方法
def __init__(self,lock=None)   构造   设置锁类型，如果不设置，则使用RLock锁
def acquire(self,blocking=True,timeout=1)  方法   获取同步锁
def wait(self,timeout=None)  方法   线程等待
def notify(self,n=1)    方法   唤醒一个等待线程对象
def notify_all(self)    方法   唤醒所有等待线程
Condition通常与一个锁进行关联，如果开发者在实例化Condition类对象时没有设置锁，则会默认使用RLock
锁对象实现锁定控制，所以在Condition类中会存有一个锁队列，同时还会存在有一个等待条件锁队列，所有执行了wait()操作的
线程都在等待条件锁队列中等待唤醒（使用notify()或notify_all()方法唤醒）

本程序中定义了一个Condition条件锁，为了方便判断当前的操作模式，所以利用一个flag变量实现生产者与消费者的操作切换，
当无法生产或无法消费时，将利用wait()方法将当前线程设置为阻塞状态，当某一操作完毕，则可以使用notify()或notify_all()方法唤醒等待线程



wait是指在一个已经进入了同步锁的线程内，让自己暂时让出同步锁，以便其他正在等待此锁的线程可以得到同步锁并运行，
只有其他线程调用了notify方法（notify并不释放锁，只是告诉调用过wait方法的线程可以去参与获得锁的竞争了，
但不是马上得到锁，因为锁还在别人手里，别人还没释放），调用wait方法的一个或多个线程就会解除wait状态，
重新参与竞争对象锁，程序如果可以再次得到锁，就可以继续向下运行。
"""
#使用Condition实现生产者与消费者模型数据同步操作
import threading, time 					# 导入线程实现模块
class Message: 						# 消息保存类
    def __init__(self, condition): 				# 构造方法
        self.__title = None 					# 初始化属性
        self.__content = None 					# 初始化属性
        self.__condition = condition				# 实例化锁
        # flag用于进行生产者和消费者线程的切换：True可以生产（不能消费），False可以消费（不能生产）
        self.__flag = True  					# 默认可以生产
    def set_info(self, title, content): 				# 属性设置
        self.__condition.acquire()				# 获取同步锁
        if self.__flag == False: 				# 判断当前状态
            self.__condition.wait()				# 当前线程等待
        self.__title = title 					# 设置数据
        time.sleep(1) 					# 模拟操作延迟
        self.__content = content				# 设置数据
        print("【%s】title = %s、content = %s" % (threading.current_thread().name,
                self.__title, self.__content)) 			# 信息输出
        self.__flag = False   					# 无法生产
        self.__condition.notify()    				# 唤醒等待线程
        self.__condition.release()  # 释放锁

    def __str__(self):    					# 获取对象信息
        self.__condition.acquire()   				# 获取同步锁
        if self.__flag == True:  				# 判断当前状态
            self.__condition.wait()   				# 当前线程等待
        try: 						# 捕获可能产生的异常
            time.sleep(0.8)  					# 模拟操作延迟
            return "〖%s〗title = %s、content = %s" % (threading.current_thread().name,
                    self.__title, self.__content) 			# 返回信息
        finally: 						# 终会执行的代码
            self.__flag = True					# 无法消费
            self.__condition.notify()   				# 唤醒等待线程
            self.__condition.release()				# 释放锁
def producer_handle(message): 					# 生产者线程处理函数
    for num in range(50):  					# 生产50次数据
        if num % 2 == 0:  					# 交替生产
            message.set_info("李兴华", "软件技术讲师")  		# 生产数据一
        else: 						# 条件不满足
            message.set_info("yootk", "www.yootk.com")		# 生产数据二
def consumer_handle(message):  				# 消费者线程处理函数
    for num in range(50):  					# 消费50次数据
        print(message) 					# 输出信息
def main():						# 主函数
    condition = threading.Condition()    			# 实例化条件锁
    message = Message(condition)  				# 实例化Message类对象
    producer_thread = threading.Thread(target=producer_handle, name="生产者线程", args=(message,))
    consumer_thread = threading.Thread(target=consumer_handle, name="消费者线程", args=(message,))
    producer_thread.start()					# 启动生产者线程
    consumer_thread.start()					# 启动消费者线程
if __name__ == "__main__":					# 判断程序执行名称
    main()


