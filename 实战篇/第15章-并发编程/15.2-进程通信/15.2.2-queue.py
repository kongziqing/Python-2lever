"""
队列是一种实用的数据缓冲机制，为了解决因频繁的进程通信所造成的通信拥堵问题，可以引入进程队列进行数据管理，
multiprocessing.Queue是多进程编程中提供的进程队列结构，该队列采用FIFO的形式实现不同进程间的数据通信，
这样可以保证多个数据按序实现发送与接收处理，

在队列操作中往往会分为队列生产者与队列消费者，生产者主要向进程队列中保存数据，而消费者是通过队列获取数据
Queue类常用操作方法
def__init__(self,maxsize = 0,*,ctx)    构造   开辟队列，并设置队列保存的最大长度
put(self,obj,block=True,timeout=None)  方法   插入数据到队列，block为队列满时的阻塞配置（默认为True），timeout为阻塞超时时间（单位是秒）
get(self,block=True，timeout=None)      方法  从队列获取数据，block为队列空时的阻塞配置（默认为True），timeout为阻塞超时时间（单位是秒）
qsize(self)                            方法   获取队列保存数据个数
empty(self)                             方法   是否为空队列
full(self)                              方法    是否为满队列


在进行进程队列操作中主要使用的是put()与get()两个方法，这两个方法中存在优两个配置参数：阻塞（block），超时时间（timeout），这两个参数
的配置意义如下
配置一（block=True、timeout=时间）：当数据保存发现队列已满或数据取出发现队列为空时，会对当前操作进行阻塞，阻塞时间为timeout,如果过了超时时间，则抛出异常
配置二（block=False）：当数据保存发现队列已满或数据取出发现队列为空时直接抛出异常
"""
import multiprocessing, time				# 模块导入
def put_worker(queue): 				# 生产者操作函数
    for item in range(50): 				# 迭代操作
        time.sleep(1) 				# 生产延迟
        print("【%s】生产数据，item = %s" %
	 (multiprocessing.current_process().name, item)) 	# 信息提示
        queue.put("item = %s" % item) 			# 向队列写入数据
def get_worker(queue): 				# 消费者操作函数
    while True: 					# 不断重复
        try:    # 通过队列获取数据，如果超过2秒队列数据为空则抛出异常
            print("〖%s〗消费数据：%s" % (multiprocessing.current_process().name,
                   queue.get(block=True, timeout=2))) 	# 信息输出
        except: 					# 捕获异常
            pass					# 暂不处理
def main():					# 主函数
    queue = multiprocessing.Queue()			# 创建队列
    # 创建生产者与消费者进程，两个进程的处理函数都需要接收相同的队列引用
    producer_process = multiprocessing.Process(target=put_worker, name="生产者进程", args=(queue,))
    consumer_process = multiprocessing.Process(target=get_worker, name="消费者进程", args=(queue,))
    producer_process.start()				# 启动生产者进程
    consumer_process.start()				# 启动消费者进程
    consumer_process.join()				# 等待生产者进程执行完毕
    producer_process.join()				# 等待消费者进程执行完毕
if __name__ == "__main__":				# 判断程序执行名称
    main()
