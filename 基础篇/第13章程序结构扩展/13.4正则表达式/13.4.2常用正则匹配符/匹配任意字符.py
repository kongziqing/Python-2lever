"""
正则表达式在字符串处理方面提供了强大支持，处理的核心就是字符串的内容匹配，因此在正则表达式中定义有大量的匹配符号，
字符匹配的主要功能是匹配指定的字符内容，这些内容可能是一个具体的字母，数字或一些转义符，字符匹配符号如下
序号              字符匹配符号           描述
1                    x             表示匹配任意的一位字符
2                    \\            匹配转义字符'\\'
3                    \t             匹配转义字符‘\t’
4                    \n              匹配转义字符'\n'
5                    \r               匹配转义字符‘\r’
"""
import re
def main():
    str="y\n"
    pattern = "Y\n"
    print(re.match(pattern, str,re.I))  #匹配两个字符“Y”和“\n”
    print(re.match(pattern, "yootk",re.I)) #匹配更多内容失败
if __name__ == '__main__':
    main()


