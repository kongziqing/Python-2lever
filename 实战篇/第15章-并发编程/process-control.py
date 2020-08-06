"""
进程虽然属于一种不确定的状态，但是通过Process类创建多进程也可以通过提供的方法进行控制，
在多进程编程中，所有的进程都会按照既定的代码顺序执行，但是某些进行可能需要强制执行，或者由于某些问题需要被中断，
那么久可以利用Process类中提供的方法进行控制，这些方法如表所示
1.terminate(self)  关闭进程
2.is_alive(self)   判断进程是否存活
3.join(self,timeout)  进程强制执行
所有的进程对象通过start()方法启动之后都将进入到进程等待队列，如果此时某个进程需要优先执行，则可以通过join()方法进行控制
本程序创建了两个进程，主进程和process进程，process进程启动后使用join()方法定义了进程的强制执行，这样在process进程未执行完毕时，
主进程将暂时退出CPU资源竞争，并将资源交由process进程控制，进程强制运行流程图如15-5所示
"""
import multiprocessing,time
def send(msg):
    time.sleep(5)#进程操作延迟
    print("[进程ID：%s、进程名称：%s]消息发送：%s"%(multiprocessing.current_process().pid,multiprocessing.current_process().name,msg))
def main():
    process = multiprocessing.Process(target=send,name = "发送进程",args = ("www.yootk,com",))
    process.start()#启动进程
    process.join()#进程强制运行（执行完毕后向下执行）
    print("[进程ID：%s、进程名称：%s]信息发送完毕。。"%(multiprocessing.current_process().pid,multiprocessing.current_process().name))#输出进程信息
if __name__ == '__main__':
    main()
