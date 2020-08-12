"""
提示：关于"（）"作用的说明
如果在定义正则表达式时没有使用"()",则会将整体正则表达式作为一个分组
通过本程序的执行结果可以发现，此时在正则表达式中并没有使用"（）"定义，这样会将整个正则表达式作为一个分组使用
"""

# coding : UTF-8
import re						# 模块导入
def main():					# 主函数
    info = "id:yootk,phone:110120119,birthday:1978-09-19"	# 匹配字符串
    pattern = r"\d{4}-\d{2}-\d{2}"              		# 匹配生日数据
    print(re.search(pattern,info).group())      		# 整体表达式为一组
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
