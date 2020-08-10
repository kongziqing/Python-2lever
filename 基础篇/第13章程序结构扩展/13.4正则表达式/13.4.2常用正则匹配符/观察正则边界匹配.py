"""
默认情况下，正则表达式进行字符串匹配时都是由头开始匹配，但如果此时字符串的内容超过了匹配表达式定义的长度，那么超过长度之后的字符串
无法进行匹配，此时就需要设置匹配边界，边界匹配符号如表：
1.^ 设置正则匹配开始，忽略多行模式
2.$ 设置正则匹配结束，忽略多行模式
为了方便观察边界的效果，本程序使用了findall()函数将符合要求的内容进行了匹配抽取，当设置边界后表达式将只会在指定的范围内进行匹配
"""
import re
def main():
    str_a = "hello food"
    pattern_a ="fo[ol][dlk]$"#可以匹配food、fool、folk结尾内容
    print(re.findall(pattern_a,str_a,re.I))  #正则匹配
    str_b="Food is very importan."  #单词写在最前面
    pattern_b="^fo[ol][dlk]"  #可以匹配food，fool.folk结尾内容
    print(re.findall(pattern_b,str_b,re.I))#正则匹配
if __name__ == '__main__':
    main()
