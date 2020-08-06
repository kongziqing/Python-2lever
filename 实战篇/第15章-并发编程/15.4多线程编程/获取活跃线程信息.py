"""
在Python中可以创建多个线程，开发者可以利用threading模块中的两个函数获取活跃线程信息
获取当前活跃线程个数：threading.active_count()
获取活跃线程信息：threading.enumerate()，返回一个列表序列

本程序一共创建了10个子线程，再加上默认启动的主线程，在子线程未执行完后，该程序一共会有11个活跃线程
"""



import threading, time				# 导入线程实现模块
def thread_handle(delay): 				# 线程处理函数
    for num in range(5): 				# 迭代操作
        time.sleep(delay) 				# 操作延迟
        print("【%s】num = %s" % (
            threading.current_thread().getName(), num)) 	# 输出线程提示信息
def main():					# 主函数
    for item in range(10): 				# 迭代产生线程
        thread = threading.Thread(target=thread_handle, args=(1,),
                name="执行线程 - %s" % item) 		# 创建线程
        thread.start()				# 启动子线程
    print("主线程ID：%s、主线程名称：%s" % (threading.current_thread().ident,
                threading.current_thread().name)) 		# 信息输出
    print("当前活跃线程个数：%s" % threading.active_count())	# 信息输出
    print("当前活跃线程信息：%s" % threading.enumerate())	# 信息输出
if __name__ == "__main__":				# 判断程序执行名称
    main()
