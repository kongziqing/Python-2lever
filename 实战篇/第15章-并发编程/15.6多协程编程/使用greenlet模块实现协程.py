"""
使用yield实现的多协程编程需要开发者定义相关的处理函数，而后还需要手工执行send()方法，为了简化协程开发的难度，
可以使用第三方模块greenlet来完成协程，此模块是针对yield操作的封装
本程序为生产者与消费者定义了两个不同的greenlet对象，并指定了不同的处理函数，在进行切换时，直接利用switch方法即可
"""
import greenlet, time					# 单独安装模块
info = None						# 保存数据
def producer_handle():					# 生产协程处理函数
    global info 						# 使用全局变量
    for item in range(10): 					# 循环发送数据
        if item % 2 == 0: 					# 发送数据判断
            info = "title = 李兴华、content = 软件技术讲师"		# 生成数据
        else: 						# 条件不满足
            info = "title = yootk、content = www.yootk.com"		# 生成数据
        print("【生产者】%s" % info) 				# 输出提示信息
        time.sleep(1) 					# 操作延迟
        consumer_greenlet.switch()				# 切换到消费者
def consumer_handle():					# 消费协程处理函数
    while True: 						# 持续消费
        print("〖消费者〗%s" % info)  				# 消费者获取数据
        time.sleep(1)  					# 操作延迟
        producer_greenlet.switch()				# 切换到生产者
producer_greenlet = greenlet.greenlet(run=producer_handle) 		# 定义协程切换
consumer_greenlet = greenlet.greenlet(run=consumer_handle) 		# 定义协程切换
def main():						# 主函数
    producer_greenlet.switch()					# 生产者运行
if __name__ == "__main__":					# 判断程序执行名称
    main()
