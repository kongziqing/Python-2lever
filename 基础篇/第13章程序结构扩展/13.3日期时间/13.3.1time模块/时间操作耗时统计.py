"""
提示：通过CPU执行时间获取程序耗时统计
在项目开发中利用时间戳的信息实现某些操作的耗时统计处理，此时只需要在开始和结束时分别获取一次时间戳，随后通过减法计算即可
"""
# coding : UTF-8
import time   				# 导入time模块
def main():				# 主函数
    start_time = time.process_time()		# 程序启动CPU耗时统计
    print("【开始】程序启动耗时：%s" % start_time) # 打印提示信息
    info = "www.yootk.com"			# 字符串变量
    for item in range(999999): 		# 设置一个循环实现延迟操作
        info += str(item) 			# 字符串连接
    end_time = time.process_time()          	# 程序执行耗时
    print("【结束】程序执行完毕耗时：%s" % end_time) # 提示信息
if __name__ == "__main__":			# 判断程序执行名称
    main()					# 调用主函数
