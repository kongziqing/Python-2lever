"""
在线程交互模型中，为了防止数据过多造成的数据拥堵问题，往往会通过队列来进行缓冲
，在threading模块中提供了3中队列
在生产者与消费者模型中引入了线程同步处理，虽然可以保证程序执行的正确性，但是也会带来执行性能下降的问题，假设生产者线程执行速度速度较快，
而消费者线程执行速度较慢，这样生产者就需要一直等到消费者完成后才可以进行后续生产，造成执行效率低下的问题，为了解决这类问题，
可以在生产者与消费者之间设置一个数据缓冲区，生产者将生产的数据保存在缓冲区内，这样既可以保证连续生产，又可以让消费者通过缓冲区
消费数据，
数据缓冲区的实现可以依靠queue模块来实现，此模块提供了3种线程同步队列类的定义
queue.Queue:先进先出（FIFO）同步队列
queue.LifoQueue:后进先出（LIFO）同步队列
queue.PriorityQueue:优先级队列

queue模块中提供的队列都提供同步锁处理，可以直接在多线程编程中使用，常用操作方法如表
def __init__(self,maxsize=0)   构造  实例化队列并设置最大保存长度
def put(self,item,block=True,timeout=None)  方法   向队列保存数据
def get(self,block=True,timeout=None)    方法    从队列获取数据
def qsize(self)   方法   返回队列大小
def empty(self)   方法    判断是否为空队列，队列为空返回True，否则返回False
def full(self)     方法    判断对列是否已满，队列满时返回True，否则返回False
def join(self)    方法     强制等待队列为空再执行后续操作
"""
import threading, time, queue					# 导入线程实现模块
class Message: 						# 消息保存类
    def __init__(self):    					# 构造方法
        self.__title = None     				# 初始化属性
        self.__content = None   				# 初始化属性
    def set_info(self, title, content): 				# 设置属性
        self.__title = title     				# 设置数据
        time.sleep(0.1)    					# 模拟操作延迟
        self.__content = content   				# 设置数据
        print("【%s】title = %s、content = %s" % (threading.current_thread().name,
                self.__title, self.__content)) 			# 信息输出
    def __str__(self):   					# 获取对象信息
        time.sleep(1)  					# 模拟操作延迟
        return "〖%s〗title = %s、content = %s" % (threading.current_thread().name,
                self.__title, self.__content) 			# 数据返回
def producer_handle(queue):   					# 生产者线程处理函数
    for num in range(50): 					# 生产50次数据
        message = Message()					# 创建消息对象
        if num % 2 == 0:    					# 交替生产
            message.set_info("李兴华", "软件技术讲师")  		# 生产数据一
        else: 						# 条件不满足
            message.set_info("yootk", "www.yootk.com") 		# 生产数据二
        queue.put(message)  					# 追加队列
def consumer_handle(queue):  					# 消费者线程处理函数
    for num in range(50):  					# 消费50次数据
        print(queue.get())					# 通过队列获取数据
def main():						# 主函数
    work_queue = queue.Queue(5)  				# 创建操作队列
    producer_thread = threading.Thread(target=producer_handle, name="生产者线程", args=(work_queue,))
    consumer_thread = threading.Thread(target=consumer_handle, name="消费者线程", args=(work_queue,))
    producer_thread.start()   					# 启动生产者线程
    consumer_thread.start()					# 启动消费者线程
if __name__ == "__main__":					# 判断程序执行名称
    main()


