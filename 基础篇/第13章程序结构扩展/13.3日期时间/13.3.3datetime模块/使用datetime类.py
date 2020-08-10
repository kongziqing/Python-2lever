"""
datetime.datetime类是日期与时间操作类，相当于date类与time类的信息总和，利用此类可以方便地获取日期时间，datetime类的常用方法
。。。。

本程序利用datetime类获取了当前的系统时间，在进行datetime类输出时可以直接按照内置格式进行字符串转换
"""
# coding : UTF-8
from datetime import datetime 					# 导入datetime类
def main():						# 主函数
    date_obj_a = datetime.today()				# 获取当前系统日期时间
    print("当前日期时间：%s" % date_obj_a) 			# 输出当前日期时间
    date_obj_b = datetime(2017, 2, 17, 21, 15, 32) 		# 指定日期时间数据
    print("指定日期时间：%s" % date_obj_b) 			# 信息输出
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
