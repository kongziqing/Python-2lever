"""
Barrier是一种栅栏的同步管理机制，利用屏障点的同步机制实现了多进程操作的并行控制，
multiprocessing.Barrier可以保证多个进程达到某一个公共屏障点（common Barrier point）的时候才进行执行
，如果没有达到此屏障点，那么进程将持续等待，这就好比现在有一队士兵，长官要求所有士兵整理装备后分组行动，每组必须凑齐三个人后自动出发，

Barrier的作用类似于栅栏，这样既可以保证若干个进程的并行执行，又可以利用方法更新屏障点的状态进行更加方便的控制，
Barrier类的常用方法
def __init__(self,parties,action=None,timeout=None)  构建Barrier实例，其中参数parties为边界数量，action为边界处理行为
def abort(self)  中断执行
def reset(self)  重置计数
def wait(self,timeout=None) 计数等待

本程序创建了9个进程实例，并且这9个进程在执行arrangement()函数时都触发了等待操作，由于设置的栅栏边界为3，所以每当凑足3个进程后就会自动向后执行
"""
# coding:UTF-8
import multiprocessing, time				# 模块导入
def barrier_handle():				# 栅栏处理函数
    print("当前战斗组士兵整装完毕，出发执行任务 ...") 	# 信息提示
def arrangement(barrier): 				# 进程处理函数
    print("【%s】开始收拾行军准备 ..." % multiprocessing.current_process().name)
    time.sleep(2) 					# 模拟延迟时间
    barrier.wait()					# 等待栅栏唤醒
    print("【%s】装备整理完毕和同组人员出发 ..." % multiprocessing.current_process().name)
def main():					# 主函数
    barrier = multiprocessing.Barrier(parties=3, action=barrier_handle)
    process_list = [multiprocessing.Process(target=arrangement, args=(barrier,),
        name="士兵 - %s" % item) for item in range(9)] 	# 创建进程列表
    for pro in process_list: 				# 迭代进程列表
        pro.start()					# 进程启动
    for pro in process_list: 				# 迭代进程列表
        pro.join()					# 等待进程执行完毕
    barrier.abort()  				# 结束同步栅栏处理
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数

