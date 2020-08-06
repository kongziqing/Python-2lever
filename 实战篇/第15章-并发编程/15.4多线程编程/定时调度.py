"""
定时调度：定时调度是一种基于线程任务的操作管理，可以实现在某段时间任务的重复执行，
定时调度是指可以根据句设定的时间安排自动执行程序任务，Python提供了sched模块以实现定时调度，
sched模块采用单进程模式实现调度处理
本程序利用sched.scheduler类实现了调度线程的创建，每当使用enter()方法设置调度任务时，该任务会执行一次，
所以需要在调度处理函数中重复使用enter()方法才可以实现定时任务的操作。
"""


import sched, threading				# 模块导入
def event_handle(schedule): 				# 线程处理函数
    print("【%s】优拓软件学院：www.yootk.com" % threading.current_thread().name)   # 获取线程信息
    schedule.enter(delay=1, priority=0, action=event_handle, argument=(schedule,)) # 延迟1秒后执行
def main():					# 主函数
    schedule = sched.scheduler()			# 实例化调度对象
    # 线程调度操作，参数作用如下：
    # “delay=0”：调度任务启动的延迟时间，如果设置为0表示立即启动；
    # “priority=0”：多个调度任务的执行优先级，优先级越高越有可能（不是一定）先执行；
    # “action=event_handle”：设置任务调度处理函数；
    # “argument=(schedule,)”：调度处理函数相关参数（必须为可迭代对象）
    schedule.enter(delay=0, priority=0, action=event_handle, argument=[schedule,])
    schedule.run()					# 启动调度线程
if __name__ == "__main__":				# 判断程序执行名称
    main()
