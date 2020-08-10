"""
时间戳与时间元组本质上是属于系统内部的数据存储结构，但是这样的存储结构并不适合用户的阅读，所以在Python中可以对日期时间进行格式化
本程序利用格式化字符串的操作形式实现了时间元组与日期时间字符串之间的转换处理操作，在Python中，除了使用自定义转换格式外，也可以使用内置
的转换格式将时间元组转换为日期时间字符串
"""
# coding : UTF-8
import time						# 导入time模块
def main():						# 主函数
    default_time_tuple = (2017, 2, 17, 21, 15, 32, 4, 48, 0) 		# 自定义时间元祖
    print("时间元祖格式化：%s" % time.strftime("%Y-%m-%d %H:%M:%S", default_time_tuple)) 	# 提示信息
    print("获取时间元祖中的日期数据：%s" % time.strftime("%F", default_time_tuple)) 	# 提示信息
    print("获取时间元祖中的时间数据：%s" % time.strftime("%T", default_time_tuple)) 	# 提示信息
    default_date_time = "2017-02-17 21:15:32"  			# 字符串
    print("字符串转为时间戳：%s" % str(time.strptime(default_date_time, "%Y-%m-%d %H:%M:%S")))
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
