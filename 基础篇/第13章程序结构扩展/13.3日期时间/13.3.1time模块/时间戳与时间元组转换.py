"""
时间元组是Python提供的一个描述日期时间数据的基本保存结构，开发者可以获取当前的时间元组，也可以定义指定日期时间的时间元组，
时间元组的定义格式如下，
（tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,tm_yday,tm_isdst）

本程序通过time()函数获取了当前系统的时间戳，利用localtime()函数将其转为时间元组并进行输出，Python允许用户按照指定格式自定义时间元组，
使用mktime()函数可以将时间元组转为时间戳格式。

"""
# coding : UTF-8
import time 						# 导入time模块
def main():						# 主函数
    current_timestamp = time.time()				# 获取当前时间戳
    current_time_tuple = time.localtime(current_timestamp) 		# 将时间戳转为时间元祖
    print("时间戳转为时间元祖：%s" % str(current_time_tuple)) 	# 时间戳转为时间元祖
    default_time_tuple = (2017, 2, 17, 21, 15, 32, 4, 48, 0) 		# 自定义时间元祖
    print("时间元祖转为时间戳：%s" % time.mktime(default_time_tuple)) 	# 时间元祖转为时间戳
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
