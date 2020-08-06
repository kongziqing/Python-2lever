"""
本程序直接利用psutil提供的处理方法获取了当前系统磁盘的分区类型，使用率，读写IO率等相关信息
"""
import psutil 						# pip install psutil
def main():
    print("【磁盘分区】获取全部磁盘信息：%s" % psutil.disk_partitions()) # 信息输出
    print("【磁盘使用率】获取磁盘“D”使用率：%s" % str(psutil.disk_usage("d:"))) # 默认为“C”盘
    print("【磁盘IO】获取磁盘IO使用率：%s" % str(psutil.disk_io_counters())) # 信息输出
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
