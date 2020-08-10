"""
本程序通过date类获取了当前系统日期，由于date类无法通过时间元组直接获取日期数据所以先利用time模块中的mktime()方法将时间元组转为时间戳，
再通过fromtimestamp()方法获取日期数据
"""
# coding : UTF-8
from datetime import date					# 导入date模块
import time						# 导入time模块
def main():						# 主函数
    print("最小描述日期：%s、最大描述日期：%s、日期单位：%s" %
	 	 (date.min, date.max, date.resolution)) 		# 信息输出
    print("今天的日期：%s" % date.today())			# 获取当前日期
    time_tuple = (2017, 2, 17, 21, 15, 32, 4, 48, 0) 		# 定义时间元祖
    print("抽取时间元祖中的日期：%s" %date.fromtimestamp(time.mktime(time_tuple))) 	# 信息输出
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
