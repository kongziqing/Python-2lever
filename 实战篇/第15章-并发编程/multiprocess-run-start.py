"""
如果现在通过“进程对象。run（）”的形式调用run方法，实质上就表示执行当前进程
需要注意的是，run()方法不能启动直接进程，进程的启动必须依靠start（）方法，而start（）方法会自动调用run()方法
观察直接调用run()方法的进程信息
通过本程序的执行结果可以发现，由于在主进程中创建了process对象，所以此时如果执行了process.run()
则表示由主进程执行了该方法

程序执行结果：
进程ID：2288、进程名称：MainProcess（“process.run()"调用）
进程ID：128、进程名称：Yootk 进程（“process.start()”调用）
"""
import multiprocessing,time
class MyProcess(multiprocessing.Process):#自定义进程类
    def __init__(self,name):#构造方法
        super().__init__(name=name)#设置进程名称
    def run(self):#进程执行
        print("进程ID：%s、进程名称：%s"%(multiprocessing.current_process().pid,multiprocessing.current_process().name))#输出进程信息

def main():
    process = MyProcess(name="Yootk进程")  #进程类对象
    process.start()   #启动新进程
    time.sleep(5)
    process.run()     #主进程调用
if __name__ == '__main__':
    main()
