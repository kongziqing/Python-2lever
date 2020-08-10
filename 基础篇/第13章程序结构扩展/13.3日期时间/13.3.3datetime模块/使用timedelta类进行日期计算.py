"""
datetime.timedelta是可以对指定日期时间单元数据进行加法和减法计算的类，例如，可以通过datetime.timedelta计算出距离指定日期
时间几天前或几个小时后的日期时间数据

本程序通过一个datetime对象实例结合timedelta对象实例实现了30个小时后以及20天前的日期时间计算
"""
# coding : UTF-8
from datetime import datetime, timedelta 			# 导入datetime类
def main():						# 主函数
    datetime_obj = datetime(2017, 2, 17, 21, 15, 32) 		# 指定日期时间数据
    dt_obj_a = datetime_obj + timedelta(hours=30) 			# 计算30小时之后的日期时间
    dt_obj_b = datetime_obj + timedelta(days=-20) 			# 计算20天前的日期时间
    print("30个小时之后的日期时间为：%s" % dt_obj_a) 		# 信息输出
    print("20天前的日期时间为：%s" % dt_obj_b) 			# 信息输出
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
