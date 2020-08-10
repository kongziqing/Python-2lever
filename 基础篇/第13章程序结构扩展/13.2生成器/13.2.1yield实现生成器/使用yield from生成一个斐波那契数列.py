"""
在使用yield生成器的同时也可以使用"yield from iterable(可迭代对象，例如：生成器，列表，元组）"的形式返回另外一个生成器，
该语法等价于for item in interale:yield item
"""
# coding : UTF-8
def fibonacci(max = 99): 				# 斐波那契数列生成器
    num_a, num_b = 0, 1  				# 定义初始化输出值
    while num_b < max: 				# 数列生成结束条件
        yield num_b 					# 返回生成数据
        num_a, num_b = num_b, num_a + num_b  		# 数据计算
def fibonacci_wrapper(fun_iterable): 			# 生成器包装
    # 等价于：for item in iterable: yield item
    yield from fun_iterable 				# 此处必须是一个迭代对象
def main():					# 主函数
    wrap = fibonacci_wrapper(fibonacci(66)) 		# 可迭代对象包装
    for item in wrap: 				# 生成数据
        print(item, end='、') 				# 输出列表项
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
