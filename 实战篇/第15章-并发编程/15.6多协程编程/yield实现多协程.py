"""
协程（Coroutine）即协作式程序，又可以称为“微线程”或“纤程”，所有的协程都是通过线程创建的，协程与进程或线程最大的区别
是进程与线程为系统级实现，而协程为程序级实现，

协程是程序级上的处理逻辑，在Python中使用yield可以实现延缓执行的功能，所以基于yield也可以实现协程开发，
协程操作的实现主要是通过程序的协作来实现的，在任一时刻只允许一个协程在运行，所以实现协程最简单的方法就是利用yield关键字，
本程序利用yield生成器的特点实现了一个线程内部的程序交互，生产者与消费者之间依靠yield等待与接收数据，从而实现两个协程的处理操作
"""
def producer(cons): 						# 协成处理函数
    info = None						# 保存生成信息
    cons.send(info) 						# 必须首先发送一个None
    for item in range(10): 					# 循环发送数据
        if item % 2 == 0: 					# 发送数据判断
            info = "title = 李兴华、content = 软件技术讲师"		# 生产数据
        else: 						# 条件不满足
            info = "title = yootk、content = www.yootk.com"		# 生产数据
        print("【生产者】%s" % info) 				# 输出提示信息
        cons.send(info)  					# 发送数据
def consumer():						# 协程处理函数
    while True: 						# 持续消费
        receive = yield 					# 等待接收数据
        print("〖消费者〗%s" % receive)  			# 输出数据
def main():						# 主函数
    con = consumer()						# 定义消费者
    producer(con) 						# 启动生产者
if __name__ == "__main__":					# 判断程序执行名称
    main()
