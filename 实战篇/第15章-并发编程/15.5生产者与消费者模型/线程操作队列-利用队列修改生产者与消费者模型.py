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
