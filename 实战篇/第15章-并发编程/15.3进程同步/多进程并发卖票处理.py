"""
多进程的执行可以提高程序的运行效率，，而在多进程处理中往往会有并发资源的处理操作形式，
那么在这样的处理过程中就有需要进行访问同步处理，下面通过一个卖票的程序来观察多进程执行的
问题所在，假设一共有5章票要通过10个进程卖出

通过本程序执行结果可以发现，多个进程出现了重复卖票的情况，为了方便读者明显地观察程序问题，在每一次
进行售票的操作中都可以使用time.sleep(0.1)实现了字典数据获得与修改的延迟处理，而通过最终的结果可以发现，
此时卖票的数量与次数明显有错误的，而造成这种错误的根本原因在于数据的不同步，
"""
import multiprocessing, time					# 模块导入
def worker(dict, item): 					# 售票进程
    while True: 						# 持续卖票
        number = dict.get("ticket") 				# 获取字典数据
        if number > 0: 					# 当前还有票
            number -= 1 					# 修改当前票数
            print("【%s】ticket = %s" % (multiprocessing.current_process().name, number)) # 信息输出
            time.sleep(0.1)   					# 操作延迟
            dict.update({"ticket":number}) 			# 更新字典数据
        else: 						# 条件不满足
            break						# 结束循环
def main():						# 主函数
    manager = multiprocessing.Manager()				# 获取Manager对象实例
    mgr_dict = manager.dict(ticket=5) 				# 一共卖出5张票
    job_process = [multiprocessing.Process(target=worker, args=(mgr_dict, item,),
      name="售票员 - %s" % item) for item in range(10)] 		# 创建进程
    for process in job_process: 				# 循环进程列表
        process.start()					# 进程启动
    for process in job_process: 				# 循环进程列表
        process.join()  					# 进程等待执行完毕
    print("所有进程执行完毕，最终剩余票数：%s" % mgr_dict.get("ticket"))    # 观察最终剩余票数
if __name__ == "__main__":					# 判断程序执行名称
    main()
