"""
在项目开发中，一段饭吗有可能会产生若干个异常，为了保证程序可以正常执行，就需要在项目中对多个异常进行相应的处理

本程序利用input()函数实现了键盘数据的输入，并且利用int()函数将输入的字符串数据转为整形数据，此时在程序中就有可能
出现两类异常，输入的字符串不是由数字组成（ValueError异常），被除数为0（ZeroDivsionError异常），为了保证程序的正常执行，
本程序使用了两个except语句捕获异常
"""
# coding : UTF-8
def main():					# 主函数
    print("【1】****** 程序开始执行 ******") 		# 信息提示
    try: 						# 捕获可能出现的异常
        num_a = int(input("请输入第一个数字："))  		# 输入数据并转为整型
        num_b = int(input("请输入第二个数字："))  		# 输入数据并转为整型
        result = num_a / num_b  # try语句中异常之后的代码将不再执行
        print("【2】****** 数学计算：%s" % (result)) 	# 除法计算
    except ZeroDivisionError as err: 			# 当出现“ZeroDivisionError”异常时执行
        print("【except】程序出现异常：%s" % err) 		# 异常处理
    except ValueError as err: 				# 当出现“ValueError”异常时执行
        print("【except】程序出现异常：%s" % err) 		# 异常处理
    else: 						# 未出现异常时执行
        print("【else】程序未出现异常，正常执行完毕。")	# 提示信息
    finally: 					# 终会执行的代码
        print("【finally】异常统一出口！")		# 异常统一出口
    print("【3】****** 程序执行完毕 ******")		# 不管是否出现异常都执行此语句
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
