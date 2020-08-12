"""
本程序匹配了数据的右边内容，如果是右边是以字母y开头，则内容将会被取出
"""
# coding : UTF-8
import re							# 模块导入
def main():						# 主函数
    info = "id:yootk,tel:110;id:lixinghua,tel:120"			# 正则数据
    pattern = r'(?=y)(?P<name>\w+)' 				# 匹配右边为“y”的内容
    print(re.findall(pattern, info)) 				# 正则处理
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
