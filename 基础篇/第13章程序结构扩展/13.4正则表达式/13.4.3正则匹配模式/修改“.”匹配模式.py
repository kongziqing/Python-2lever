"""
本正则操作中，“.”表示任意的字符，所以在不设置re.S匹配模式时，会自动按照换行（“\n”也可以通过"."）进行匹配，但如果取消掉了“.”匹配
任意字符的限制后，可以发现此时返回的列表中只有一个元素
"""
# coding : UTF-8
import re							# 模块导入
def main():						# 主函数
    data = """
        Food is very important
        Food is very delicious
        Food needs cooking
    """  							# 多行字符串
    pattern = ".+" 						# 正则匹配符号
    print("不修改“.”匹配：%s" % re.findall(pattern, data)) 	# “.”匹配任意字符串，包括换行符
    print("修改“.”匹配：%s" % re.findall(pattern, data, re.S)) 	# 取消“.”匹配
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
