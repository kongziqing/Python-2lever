"""
datetime.time 类是进行时间信息描述的类，在该类中时间单元的基本组成为时，分，秒，微秒，time类中定义的常用属性与方法。。。

本程序实例化了time类对象，这样就可以直接利用time类中提供的isoformat()方法格式化显示时间数据
"""

# coding : UTF-8
from datetime import time					# 导入time类
def main():						# 主函数
    print("最小时间：%s、最大时间：%s、时间单位：%s（微秒）" %
	 (time.min, time.max, time.resolution)) 			# 信息输出
    time_data = time(21, 15, 32, 123678) 			# 实例化时间对象
    print("时：%s、分：%s、秒：%s、微秒：%s" %
	 (time_data.hour, time_data.minute, time_data.second, time_data.microsecond))
    print("格式化时间：%s" % time_data.isoformat())		# 获取格式化时间
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
