"""
multiprocessing提供的是一个跨平台的多进程解决方案，而在Linux、Unix操作系统中提供了一个fork（）函数，
利用此函数可以创建子进程，fork()函数的本质就是克隆已有的父线程，这样就会实现父子两个进程异步执行的操作，Python通过os.fork()函数
实现了fork()系统函数的调用，该函数有三种返回结果，子进程创建失败（返回“<0”），在子进程中获取数据（返回“=0”），在父进程中获取数据（返回>0）
注意windows系统不支持fork()函数
"""

import multiprocessing,os
def child():#子线程函数
    print("[child()]父进程ID：%s,子进程ID：%s"%(os.getppid(),os.getpid()))
def main():
    print("[main()]进程ID：%s、进程名称：%s"%(multiprocessing.current_process().pid,multiprocessing.current_process().name))
    newpid = os.fork()  #创建新线程
    print("[fork()]新的子进程ID=%s"%newpid)
    if newpid ==0:#执行子进程
        child()   #子进程执行函数
    else:
        print("父进程执行，父进程ID：%s"%os.getpid())
if __name__ == '__main__':
    main()

