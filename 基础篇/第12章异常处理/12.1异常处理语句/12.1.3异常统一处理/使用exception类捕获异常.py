"""
Python的异常处理流程：
1.在Python中可以处理的异常全部都是在程序运行中产生的，当程序执行到某行代码并且此代码产生异常时，会由Python虚拟机动态的进行相应异常
类型的对象实例化操作
2.如果此时在代码中没有提供异常处理语句，则Python虚拟机会采用默认的异常处理方式，即输出异常信息，随后中断程序的执行。
3.产生异常的代码需要定义在try语句中，如果此时项目中存在有异常处理，则该异常类的实例化独享会自动被捕获并交由except语句处理，如果
没有产生异常，则执行else语句。
4.except负责将try捕获到的异常类实例化对象进行异常类型的匹配，如果匹配成功，则进行相应的异常处理，如果没有匹配成功，则继续匹配后续
的except异常类型，如果所有异常类型都不匹配，则表示该异常无法处理。
5.不管是否产生异常，最终都要执行finally语句，当执行完finally语句后，程序会进一步判断当前的异常是否已经被处理了，如果已经处理
完毕，则继续执行其他代码，如果没有处理，则交由Python虚拟机进行默认处理
默认分析可以发现在整个的异常处理流程中，所有的操作围绕的是一个异常类的实例化对象，那么那个异常类的实例化对象的类型就成了理解异常
处理的核心关键所在，之前接触过的两种异常继承关系
                                    object<---BaseException
         ____________________________________________|
        |             |             |               |
KeyboardInterrupt  SystemExit  GeneratorExit   Exception <---- ArithmeticError
                                                    ^              ^
                                                    |              |
                                               ValueError   ZeroDivisionError
可以发现Python中的异常全部都继承自BaseException父类，程序中可以处理的异常全部都是Exception子类，按照对象的多态性原则，
此时except语句就可以利用Exception类来简化异常捕获操作
"""

# coding : UTF-8
def main():					# 主函数
    print("【1】****** 程序开始执行 ******")  		# 信息提示
    try: 						# 捕获可能出现的异常
        num_a = int(input("请输入第一个数字："))  		# 输入数据并转为整型
        num_b = int(input("请输入第二个数字：")) 		# 输入数据并转为整型
        result = num_a / num_b 			# try语句中异常之后的代码将不再执行
        print("【2】****** 数学计算：%s" % (result))  	# 除法计算
    except Exception as err:  				# 当出现异常时执行
        print("【except】程序出现异常：%s" % err) 		# 异常处理
    else: 						# 未出现异常时执行
        print("【else】程序未出现异常，正常执行完毕。")	# 信息输出
    finally: 					# 终会执行的代码
        print("【finally】异常统一出口！")		# 异常统一出口
    print("【3】****** 程序执行完毕 ******")		# 不管是否出现异常都执行此语句
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
