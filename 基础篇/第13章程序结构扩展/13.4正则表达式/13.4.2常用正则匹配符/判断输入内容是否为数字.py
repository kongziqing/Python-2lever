"""
在进行正则表达式定义中，为了描述更加复杂的匹配结构，也可以通过括号（）将若干个匹配符号定义在一起，
这样就可以为这个整体的表达式定义量词
"""
import re
def main():
    input_data = input("输入考试成绩：")
    #如果此时在字符串前定义r,那么正则表达式编写为““^[+-]?\\d+(\\.\\d+)?$””,符号都需要转移处理
    pattern = r"^[+-]?\d+(\.\d+)?$"
    if re.match(pattern,input_data,re.I):
        print("成绩数据输入正确，内容为：%s"%input_data)
    else:
        print("成绩数据输入错误！")
if __name__ == '__main__':
    main()