"""
在一些程序场景中多个线程之间是需要进行通信的，如果要考虑到执行顺序的问题，就必须在两个线程上进行处理，
在线程开发中有一个基础的生产者与消费者模型
本程序利用多线程实现了一个基本的线程交互模型，在程序中生产者与消费者拥有同一个message实例，
但是通过程序的执行结果可以发现，此时生产者与消费者存在以下两个问题
数据错位：假设生产者线程刚想数据存储空间添加了信息的名称，但还没有加入该信息的内容，
此时如果程序切换到了消费者线程，消费者线程将把这条信息的名称和上一条信息的内容联系到一起
重复操作：一个情况是生产者放了若干次的数据后，消费者才开始取数据，另一种情况是消费者取完一个数据后，还没等到生产者放入新的数据，
又重复取出已取过的数据
"""
import threading, time					# 导入线程实现模块
class Message: 						# 消息保存类
    def __init__(self): 					# 构造方法
        self.__title = None					# 初始化属性
        self.__content = None 					# 初始化属性
    def set_info(self, title, content): 				# 属性设置
        self.__title = title 					# 设置数据
        time.sleep(1) 					# 模拟操作延迟
        self.__content = content				# 设置数据
        print("【%s】title = %s、content = %s" % (threading.current_thread().name,
                self.__title, self.__content)) 			# 输出提示信息
    def __str__(self):  					# 获取对象信息
        time.sleep(0.8) 					# 模拟操作延迟
        return "〖%s〗title = %s、content = %s" % (threading.current_thread().name,
                self.__title, self.__content) 			# 返回数据信息
def producer_handle(message): 					# 生产者线程处理函数
    for num in range(50): 					# 生产50次数据
        if num % 2 == 0: 					# 交替生产
            message.set_info("李兴华", "软件技术讲师")		# 生产数据一
        else: 						# 条件不满足
            message.set_info("yootk", "www.yootk.com")		# 生产数据二
def consumer_handle(message): 					# 消费者线程处理函数
    for num in range(50):    					# 消费50次数据
        print(message) 					# 输出信息
def main():						# 主函数
    message = Message()  					# 实例化Message类对象
    producer_thread = threading.Thread(target=producer_handle, name="生产者线程", args=(message,))
    consumer_thread = threading.Thread(target=consumer_handle, name="消费者线程", args=(message,))
    producer_thread.start()					# 启动生产者线程
    consumer_thread.start()					# 启动消费者线程
if __name__ == "__main__":					# 判断程序执行名称
    main()
