"""
使用group()函数需要通过索引来获取数据，但是在分组过多时候就有可能造成索引混乱的问题，为了解决这一问题，用户可以在进行分组时
对分组进行命名，然后就可以直接通过分组名称获取数据

本程序在进行分组时使用"?P<名称>"（大写字母P）为每一个分组定义了名称，这样group()函数就可以进行名称获取数据
"""

# coding : UTF-8
import re							# 模块导入
def main():						# 主函数
    info = "id:yootk,phone:110120119,birthday:1978-09-19"		# 匹配字符串
    pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})" 	# 匹配生日数据，进行数据分组
    match = re.search(pattern,info) 				# 正则处理
    print("获取“year”数据：%s" % match.group("year"))		# 根据名称获取内容
    print("获取“month”数据：%s" % match.group("month")) 		# 根据名称获取内容
    print("获取“day”数据：%s" % match.group("day")) 		# 根据名称获取内容
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
