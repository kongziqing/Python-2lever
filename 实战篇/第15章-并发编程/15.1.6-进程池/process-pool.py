"""
进程池的主要设计思想是将系统可用的进程对象放在一个对象池中进行管理，当需要创建子进程时，就通过该进程池获取一个进程对象
然而进程池中的对象并不是无限的，当进程池无可用对象时，新的进程将进入到阻塞队列进行等待，一直等到其他进程执行完毕将进程归还
到进程池后才可以继续执行，进程池操作原理如图15-9所示
Pool类常用操作方法
apply(self,func,args=(),kwds = {})  采用阻塞模式创建进程并接受返回结果
apply_async(func[,args[,kwds[,callback]]])  采用非阻塞模式创建进程，并且可以接受工作函数返回结果
apply_async(self,func,args=(),kwds={})  采用非阻塞式模式进行数据处理
map_async(self,func,iterable) 采用非阻塞模式进行数据处理
close(self)  关闭进程池，不再接受新的进程
terminate(self) 中断进程
join(self)  进程强制执行
"""
"""
本程序创建了一个两个大小的进程池（Pool(processes=2)）,这样所有通过apply_async()方法创建的子进程
会共享进程池中的资源，同时这些进程会采用非阻塞的方式执行，为了防止主函数提前结束，所以在程序中使用pool.join()等待
进程池任务全部执行完并关闭后才会继续执行后续代码
"""
import multiprocessing, time					# 模块导入
def work (item): 						# 进程处理函数
    time.sleep(1) 						# 延迟
    return "【工作进程ID：%s、工作进程名称：%s】item = %s" % (
        multiprocessing.current_process().pid,
        multiprocessing.current_process().name, item) 		# 返回进程信息
def main():						# 主函数
    pool = multiprocessing.Pool(processes=2) 			# 定义2个大小的进程池
    for item in range(10): 					# 创建10个进程
        result = pool.apply_async(func=work, args=(item,)) 		# 非阻塞形式执行进程
        print(result.get())					# 获取进程返回结果
    pool.close()  						# 执行完毕后关闭进程池
    pool.join()						# 等待进程池执行完毕
if __name__ == "__main__":					# 判断程序执行名称
    main()
