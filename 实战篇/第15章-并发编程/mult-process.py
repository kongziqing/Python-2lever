"""
process类的常用属性和方法
1.pid 获取进程ID
2.name 获取进程名称
3.def__init__([group[,target[,name[,args[,kwargs,[,daemon]]]]]])
    *group:分组定义
    *target：进程处理对象（代替run（）方法）
    *name：进程名称，若不设置，则自动分配一个名称
    *args：进程处理对象所需要的执行参数
    *kwargs:调用对象字典
    *daemon：是否设置为后台进程
4.start(self) 进程启动，进入进程调度队列
5.run(self) 进程处理(不指定target时起效)
在创建多进程时可以单独设置进程的处理函数（target参数），也可以定义多进程执行类，在进行进程处理时可以通过multiprocessing.current_process()
函数动态获取当前执行的进程对象，由于多进程的执行状态是不确定的，所以每一个进程的名称就成为了唯一的区分标记，在进行多进程名称定义时一定要在
进程启动前设置名称，并且不能重名，同时已经启动的进程不能修改名称
"""
import multiprocessing,time  #模块导入
def worker(delay,count):#设置进程处理函数
    for num in range(count):#迭代输出
        print("[%s]进程ID：%s、进程名称：%s"%(num,multiprocessing.current_process().pid,multiprocessing.current_process().name))#输出进程信息
        time.sleep(delay)  #延迟，减缓程序执行

def main():  #主函数
    for item in range(3):  #创建3个进程
        # 创建进程对象，将worker函数设置为进程处理函数，args表示worker函数需要接收的参数
        process = multiprocessing.Process(target=worker,args=(1,10),name="Yootk进程-%s"%item)
        process.start() #进程启动
if __name__ == '__main__':
    main()



