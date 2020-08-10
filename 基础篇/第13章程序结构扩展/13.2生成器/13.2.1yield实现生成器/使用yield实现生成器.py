"""
本程序利用yield实现了一个主键生成器，此时的生成器操作在每一次执行for循环时才会执行并返回数据，所以不会造成占用过多内存的问题，
从而提升了程序执行性能

"""
# coding : UTF-8
def generator(maxnum): 				# 生成器
    for num in range(1, maxnum): 			# 不会一次性生成
        yield "yootk-{num:0>20}".format(num=num) 		# yield返回生成结果
def main():					# 主函数
    for item in generator(10): 			# for循环调用
        print(item) 					# 直接输出生成器返回结果
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
