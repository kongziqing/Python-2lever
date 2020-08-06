"""
不同进程之间通过管道频繁地进行交互对程序的开发很不利，为了简化进程数据通信的操作，
python提供了Manager类，利用此类可以实现进程间列表和字典数据的共享操作。
在Python中，为了更加方便的实现多进程的数据共享支持，multiprocessing模块提供了一种数据共享
进程的实现，该类进程可以通过Manager类创建，主要支持有两类操作数据形式，列表（list）,字典（dict）

本程序获取了一个Manager类的实例化对象，随后利用此对象构造了一个可以使用于进程共享的列表集合，这样多个进程将可以对同一个列表的数据
进行操作
"""

# coding:UTF-8
import multiprocessing,time						# 模块导入
def worker(list, item): 						# 数据处理函数
    list.append("【%s】item = %s" % (multiprocessing.current_process().name, item)) # 信息提示
def main():							# 主函数
    manager = multiprocessing.Manager()					# 获取Manager对象实例
    main_item = "【%s】www.yootk.com" % multiprocessing.current_process().name
    mgr_list = manager.list([main_item]) 				# 创建共享列表
    job_process = [multiprocessing.Process(target=worker, args=(mgr_list, item,),
	name="数据操作进程 - %s" % item) for item in range(3)] 		# 创建3个进程
    for process in job_process: 					# 循环进程列表
        process.start()						# 进程启动
    for process in job_process: 					# 循环进程列表
        process.join()						# 进程等待执行完毕
    print("所有进程执行完毕，列表最终数据：%s" % mgr_list) 			# 输出处理后的列表内容
if __name__ == "__main__":						# 判断程序执行名称
    main()								# 调用主函数
