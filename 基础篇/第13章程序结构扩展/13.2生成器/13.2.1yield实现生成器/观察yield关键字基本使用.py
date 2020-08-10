"""
yield主要是用于生成器操作中，与传统的操作相比，yield的最大特点在于不会生成全部的数据，而是根据数据需要动态的控制生成器的数据，
这样的好处是避免生成的数据占用过多的内存，从而影响到程序的执行性能，yield的作用于return类似，最大的区别在于，yield调用时需要通过
外部提供的next()控制，当调用next()方法后才可以出发yield返回数据，同时外部也可以利用"生成器对象.send()"方法想yield调用处发送信息，并返回下一次
的yield内容，
"""
# coding : UTF-8
def generator():					# 生成器
    print("【generator()】yield代码执行前。") 		# 提示信息
    res = yield "yootk-001" 				# 返回数据并接收发送来的内容
    print("【generator()】yield代码执行后，res = %s" % res) 	# 接收到发送来的数据后继续执行
    yield "yootk-%s" % res				# 返回数据
def main():					# 主函数
    result = generator()				# 获取生成器对象
    print("【main()】调用next()函数获取yield返回内容：%s" % next(result)) 	# 接收yield返回数据
    print("【main()】向yield发送数据：%s" % result.send(125)) 		# yield发送并返回数据
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
