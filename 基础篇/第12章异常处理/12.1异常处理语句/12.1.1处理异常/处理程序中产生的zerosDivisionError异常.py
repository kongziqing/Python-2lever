"""
本程序将有可能产生异常的语句定义在了try语句中，这样，当程序产生异常时会自动匹配相应的except语句进行异常处理
异常处理除了使用try-except结构外，也可以使用try。。。except。。。finally结果，使用后者可以定义异常处理的统一出口，
这样，在程序执行时无论是否出现异常都会执行finally语句
"""
# coding : UTF-8
def main():					# 主函数
    print("【1】****** 程序开始执行 ******") 		# 信息提示
    try: 						# 捕获可能出现的异常
        result = 10 / 0 				# try语句中异常之后的代码将不再执行
        print("【2】****** 数学计算：%s" % (result)) 	# 除法计算
    except ZeroDivisionError as err: 			# 当出现“ZeroDivisionError”异常时执行
        print("程序出现异常：%s" % err) 			# 异常处理
    print("【3】****** 程序执行完毕 ******")		# 信息提示
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
