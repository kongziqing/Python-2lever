"""
本程序直接通过date类的构造方法构造了一个自定义的日期对象，随后可以利用date类中的方法直接获取该日期的元组，格式化，星期数等内容

"""
# coding : UTF-8
from datetime import date					# 导入date类
import time						# 导入time模块
def main():						# 主函数
    default_date = date(2017, 2, 17) 				# 构造date类实例
    print("返回星期数：%s、返回ISO星期数：%s" %
	 (default_date.weekday(), default_date.isoweekday()))	# 信息输出
    print("格式化日期显示：%s" % default_date.isoformat())		# 信息输出
    print("日期元祖：%s" % str(default_date.isocalendar()))		# 信息输出
    print("日期替换：%s" % default_date.replace(1987, 9, 15)) 	# 信息输出
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
