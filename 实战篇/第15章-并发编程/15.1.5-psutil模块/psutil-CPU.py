"""
通过psutil模块分别获取CPU的物理数量与逻辑数量，同时利用该模块也可以准确地获取CPU的使用率信息，在进行系统管理过程中
经常需要对CPU的状态进行监控，所以本程序利用for循环并结合psutil.cpu_percent()方法每隔1秒获取当前系统中的CPU占用率嘻嘻
"""
import psutil
def main():
    print("[理CPU数量：%d"%psutil.cpu_count(logical=False))#提示信息
    print("逻辑CPU数量：%d"%psutil.cpu_count(logical=True))#提示信息
    print("用户CPU使用时间：%f、系统CPU使用时间：%f、CPU空闲时间：%f"%(psutil.cpu_times().user,psutil.cpu_times().system,psutil.cpu_times().idle))  #提示信息
    for x in range(10):#循环监控CPU信息，每一秒获取一次CPU信息，一共获取10次信息
        print("CPU使用率监控：%s"%psutil.cpu_percent(interval=1,percpu=True))
if __name__ == '__main__':
    main()