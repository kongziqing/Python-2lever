"""
利用psutil模块关闭指定的功能进程,关闭微信进程WeChat.exe
"""
import psutil   #主函数
def main():
    for proc in psutil.process_iter():#获取全部系统进程
        try:
            if proc.name() == "WeChat.exe":
                proc.terminate()  #进程强制结束
                print("发现wechat.ext程序进程，已经强制关闭")#提示信息
        except  psutil.NoSuchProcess:#异常处理
            pass #未定义具体操作
if __name__ == '__main__':
    main()