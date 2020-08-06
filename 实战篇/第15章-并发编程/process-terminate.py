"""
多进程的执行中，一个进程可以被另外一个进程中断执行，此时只需要获取相应的进程对象并调用teminate()方法即可
本程序定义二楼一个process进程，但是在该进程执行过程中，使用主进程实现了进程的中断，由于不确定进程的执行转态，所以在中断前
先使用is_alive()方法判断进程是否处于存活状态
"""
import multiprocessing,time
def send(msg):
    time.sleep(10)#进程操作延迟
    print("[进程ID：%s、进程名称：%s]消息发送：%s"%(multiprocessing.current_process().pid,multiprocessing.current_process().name,msg))#输出进程信息
def main():
    process= multiprocessing.Process(target=send,name="发送进程",args=("www.yootk,com",))
    process.start()#启动进程
    time.sleep(2)#保证进程先运行一会儿
    if process.is_alive():#进程还存活
        process.terminate()#进程中断自行
        print("”%s“进程执行被中段，，，"%process.name)#输出提示信息
if __name__ == '__main__':
    main()