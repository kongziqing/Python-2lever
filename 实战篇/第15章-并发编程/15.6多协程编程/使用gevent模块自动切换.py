"""
虽然greenlet组件可以实现多协程开发，但是需要由开发者明确地获取指定的切换对象后才可以进行处理，
这样的操作会比较麻烦，而在第三方Python模块中还提供了一个gevent模块，利用此模块还可以实现自动切换处理

本程序利用gevent分别设置了两个协程管理对象，只需要使用sleep()方法就可以自动实现不同协程的操作
"""
import gevent					# pip install gevent
info = None					# 保存数据
def producer_handle():				# 协程处理函数
    global info					# 使用全局变量
    for item in range(10): 				# 循环发送数据
        if item % 2 == 0: 				# 发送数据判断
            info = "title = 李兴华、content = 软件技术讲师"	# 数据生产
        else: 					# 条件不满足
            info = "title = yootk、content = www.yootk.com"	# 数据生产
        print("【生产者】%s" % info) 			# 输出提示信息
        gevent.sleep(1) 				# 切换延迟
def consumer_handle():				# 协程处理函数
    for item in range(10): 				# 迭代生成数据
        print("〖消费者〗%s" % info) 			# 消费者获取数据
        gevent.sleep(1) 				# 切换延迟
def main():					# 主函数
    producer_gevent = gevent.spawn(producer_handle) 	# 创建协程对象
    consumer_gevent = gevent.spawn(consumer_handle) 	# 创建协程对象
    producer_gevent.join()				# 协程启动
    consumer_gevent.join()				# 协程启动
if __name__ == "__main__":				# 判断程序执行名称
    main()
