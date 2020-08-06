"""
在多进程编程中为了方便进程操作的统一管理，也可以将进程的执行操作封装在一个类中，此进程操作类要求继承Process父类
，同时需要将该进程类的执行操作定义在run()方法中

本程序将进程的操作封装在了MyProcess类中，并且在run()方法内定义了进程的相关操作代码，但是，需要注意的是，run()方法不能启动直接进程，
进程的启动必须依靠start()方法，而start()方法会自动调用run方法
"""
import multiprocessing,time #模块导入
class Myprocess(multiprocessing.Process):#进程处理类
    def __init__(self,name,delay,count):#构造方法
        super().__init__(name=name) #调用父类构造，设置进程名称
        self.__delay = delay  #进程操作延迟
        self.__count = count  #循环次数
    def run(self):   #进程运行方法
        for num in range(self.__count):#迭代输出
            print("[%s]进程ID：%s、进程名称：%s"%(num,multiprocessing.current_process().pid,multiprocessing.current_process().name))
            time.sleep(self.__delay)#延迟，减缓程序执行
def main():
    for item in range(3):#迭代运行
        process = Myprocess(name="Yootk进程-%s"%item,delay=1,count=10) #创建进程对象
        process.start() #进程启动，调用run()
if __name__ == '__main__':
    main()  #调用主函数