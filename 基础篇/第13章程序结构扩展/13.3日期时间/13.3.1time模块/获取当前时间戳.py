"""
本程序在for循环开始前通过time()函数获取了相应的时间戳数据，这样，在程序执行完毕只需要将开始和结束时获取的两个时间戳的信息
进行减法操作就可以得出本次操作所耗费的时间
"""
# coding : UTF-8
import time					# 导入time模块
def main():					# 主函数
    start_timestamp = time.time()			# 操作开始前获取时间戳
    print("【开始】程序执行开始时间戳：%s" % start_timestamp)# 提示信息
    info = "www.yootk.com"				# 定义变量
    for item in range(999999): 			# 设置一个循环实现延迟操作
        info += str(item) 				# 字符串连接
    end_timestamp = time.time()			# 操作结束后获取时间戳
    print("【结束】程序执行完毕时间戳：%s" % end_timestamp) 	# 提示信息
    print("【统计】本次操作执行所花费的时间为：%5.2f秒。" % (end_timestamp - start_timestamp))
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
