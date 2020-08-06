"""
本程序利用Manager类对象创建了一个字典集合，这样多进程处理函数就可以共享一个字典集合同时实现数据的更新
"""
import multiprocessing,time					# 模块导入
def worker(dict, item): 					# 数据处理函数
    dict.update({multiprocessing.current_process().name: item}) 	# 为字典追加数据
def main():						# 主函数
    manager = multiprocessing.Manager()				# 获取Manager对象实例
    mgr_dict = manager.dict(main_name="www.yootk.com") 		# 创建共享字典
    job_process = [multiprocessing.Process(target=worker, args=(mgr_dict, item,),
	name="数据操作进程 - %s" % item) for item in range(3)] 	# 创建三个进程
    for process in job_process: 				# 循环进程列表
        process.start()					# 进程启动
    for process in job_process: 				# 循环进程列表
        process.join()					# 进程等待执行完毕
    print("所有进程执行完毕，列表最终数据：%s" % mgr_dict) 		# 输出处理后的列表内容
if __name__ == "__main__":					# 判断程序执行名称
    main()
