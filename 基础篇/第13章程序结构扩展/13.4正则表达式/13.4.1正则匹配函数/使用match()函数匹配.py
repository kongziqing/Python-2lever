"""
re模块常用函数
compile(pattern,flags=0)    编译正则表达式
escape(pattern)     正则符号转义处理
findall(pattern,string,flags=0)     匹配正则符号，并且将匹配的内容以列表的形式返回
finditer(pattern,string,flags=0)    匹配正则符号，并且将匹配的内容以迭代对象的形式返回
match(pattern,string,flags=0)       从头开始进行匹配
purge()     清除缓存中的正则表达式
search(pattern,string,flags=0)      在任意位置上进行匹配
split(pattern,string,maxsplit=0,flags=0)    按照给定匹配符号拆分字符串
sub(pattern,repl,string,count=0,flags=0)   正则匹配替换，count表示替换次数
subn(pattern,repl,string,count=0,flags=0)   正则匹配替换，并返回替换结果


这些函数的主要功能就是进行正则的匹配（查找），查分，和替换等操作，同时这些函数也可以进行子字符串的匹配处理，

使用match()函数会从头进行匹配，如果匹配成功，则会返回有一个Match类的对象，在该对象中可以使用span()函数获取匹配的索引元组对象，
如果匹配不成功，则会返回None
"""

# coding : UTF-8
import re								# 模块导入
def main():							# 主函数
    print("从头匹配：%s" % re.match("yootk", "yootk.com"))			# 正则匹配
    print("从头匹配：%s" % str(re.match("yootk", "yootk.com").span()))		# 正则匹配
    print("不匹配：%s" % re.match("小李老师", "yootk.com"))			# 正则匹配
    print("忽略大小写匹配：%s" % re.match("YOOTK", "yootk.com", re.I)) 		# re.I表示忽略大小写
if __name__ == "__main__":						# 判断程序执行名称
    main()								# 调用主函数
