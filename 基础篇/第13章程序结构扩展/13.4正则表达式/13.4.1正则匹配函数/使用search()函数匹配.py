"""
search()函数与match()函数最大的区别在于可以匹配一个字符串中的任意位置，同时也会返回匹配结果的索引位置
"""

# coding : UTF-8
import re								# 模块导入
def main():							# 主函数
    print("字符串匹配：%s" % re.search("yootk", "www.yootk.com"))		# 匹配任意位置
    print("字符串匹配：%s" % re.search("YOOTK", "www.yootk.com", re.I)) 	# 忽略大小写匹配
if __name__ == "__main__":						# 判断程序执行名称
    main()								# 调用主函数
