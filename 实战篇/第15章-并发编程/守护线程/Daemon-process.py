"""
在项目中除了处理核心业务的进程外，还会提供一些后台的辅助进程，这样的进程被称为守护进程，守护进程可以提供
非核心业务之外的支持服务数据，
守护进程是一种运行在后台的特殊进程，守护进程为专属的进程服务，并且当该专属进程中断后，守护进程也同时中断，
在开发中可以利用守护进程做一些特殊的系统任务，例如，如果现在要搭建一个HTTP服务器，则一定要有一个专属的HTTP请求处理的工作进程，
同时为了监控该工作进程的状态，可以为其配置一个守护进程，所有的监控服务器通过守护进程就可以确定服务器的状态

本程序为worker_process创建了一个守护进程，这样在该进程存活过程中守护进程将一直子后台工作，当工作进程结束后，守护进程也同时销毁
"""
import time,multiprocessing  #守护进程处理函数
def status():  #守护进程处理函数
    item=1   #定义变量进行累加统计
    while True:#持续运行
        print("[守护进程ID：%s、守护进程名称：%s]item = %s"%
              (multiprocessing.current_process().pid,multiprocessing.current_process().name,item))#输出进程信息
        item+=1   #数据累加
        time.sleep(1)   #延迟
def worker():   #工作进程处理函数
    #为工作进程创建一个守护进程，只需要工作进程不结束，守护进程将一直在后台运行
    daemon_process = multiprocessing.Process(target=status,name = "守护进程",daemon=True)
    daemon_process.start()  #启动守护进程
    for item in range(10):#工作进程运行期间，守护进程始终存在
        print("[工作进程ID：%s、工作进程名称：%s] item = %s"%
              (multiprocessing.current_process().pid,multiprocessing.current_process().name, item))  #输出进程信息
        time.sleep(2) #延迟

def main():
    worker_process = multiprocessing.Process(target=worker,name = "工作进程")
    worker_process.start()  #启动工作进程
if __name__ == '__main__':
    main()  #调用主函数
