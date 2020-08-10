"""
本程序利用asctime()函数采用内置的结构将时间元组格式化，如果没有设置时间元组，则将会通过localtime（）函数获取当前系统时间元组并进行转换，

时间戳  ---->ctimed()----->格式化字符串
时间戳 ---->localtime(),gmtime()------>时间元组

时间元组------>mktime()----->时间戳
时间元组----->asctime(),strftime()--->格式化字符串

格式化字符串----->strptime()------>时间元组



"""
# coding : UTF-8
import time						# 导入time模块
def main():						# 主函数
    print(time.asctime())					# 获取当前日期时间
    print(time.asctime((2017, 2, 17, 21, 15, 32, 4, 48, 0))) 		# 时间元祖转换
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
