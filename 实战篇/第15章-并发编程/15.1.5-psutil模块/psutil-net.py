import psutil 						# pip install psutil
def main():
    print("【数据统计】网络数据交互信息：%s" % str(psutil.net_io_counters()))	# 信息输出
    print("【接口统计】网络接口信息：%s" % str(psutil.net_if_addrs()))	# 信息输出
    print("【接口状态】网络接口状态：%s" % str(psutil.net_if_stats()))	# 信息输出
if __name__ == "__main__":					# 判断程序执行名称
    main()
