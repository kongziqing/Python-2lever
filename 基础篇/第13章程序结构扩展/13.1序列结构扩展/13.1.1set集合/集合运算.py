"""
使用set集合存储数据又一个最为重要的操作就是可以进行集合的运算处理，实现"交集"“差集”“并集”的计算
本程序直接利用字符串定义了两个set集合，随后分别利用set类提供的方法和简化符号实现了集合的运算
"""
# coding : UTF-8
def main():						# 主函数
    set_a = set("abcd") 					# 定义set集合，并保存序列数据
    set_b = set("acxy")					# 定义set集合，并保存序列数据
    print("【交集】方法计算：%s、符号计算：%s" % (set_a.intersection(set_b) , set_a & set_b))
    print("【差集】方法计算：%s、符号计算：%s" % (set_a.difference(set_b) , set_a - set_b))
    print("【对称差集】方法计算：%s、符号计算：%s" % (set_a.symmetric_difference(set_b) , set_a ^ set_b))
    print("【并集】方法计算：%s、符号计算：%s" % (set_a.union(set_b) , set_a | set_b))
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
