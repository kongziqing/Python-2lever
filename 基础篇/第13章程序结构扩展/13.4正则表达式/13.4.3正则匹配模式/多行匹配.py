"""
在正则匹配中除了正则符号与操作函数之外，最为重要的就是匹配模式，利用匹配模式可以对传统正则标记的功能进行补充，
在进行正则表达式匹配时也可以通过正则匹配模式进行匹配控制，例如在之前使用过的re.I就属于一种匹配模式，re模块中定义的
正则匹配模式如表所示
1.I,IGNORECASE  常量  忽略大小写
2.L，LOCALE  常量  字符集本地化表示，可以匹配不同语言环境下的符号
3.M,MULTILINE 常量，多行匹配模式
4.S,DOTALL 常量，修改"."匹配任意模式，可匹配任意字符，包括换行符
5.X，VERBOSE 常量  此模式忽略正则表达式中的空白和注释
6.U，UNICODE 常量  \w,\W,\b,\B,\d,\D,\s,\S这些匹配符号将按照Unicode定义

这些正则匹配模式在开发中可以单独使用，也可以使用“|”进行若干个匹配模式的共同设置

本程序使用了两个正则匹配模式re.I |re.M (忽略大小写以及多行匹配)，这样会自动换行作为分隔符，匹配多行字符串中每一行的内容
"""
# coding : UTF-8
import re						# 模块导入
def main():					# 主函数
    data = """
        Food is very important
        Food is very delicious
        Food needs cooking
    """ 						# 多行字符串
    pattern = "fo{2}d"  				# 正则匹配符号
    result = re.findall(pattern, data, re.I | re.M) 	# 忽略大小写并且支持多行匹配
    print("匹配多行字符串首部：%s" % result) 		# 信息输出
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
