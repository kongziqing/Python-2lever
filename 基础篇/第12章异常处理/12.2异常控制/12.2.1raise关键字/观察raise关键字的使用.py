"""
观察raise关键字的使用
异常产生后，Python会自动实例化指定异常类的对象，以方便用户进行异常处理，但是在一些时候开发者也可以手工实例化异常类对象，
并通过raise关键字抛出异常
本程序中使用raise关键字手工抛出了一个异常类的实例化对象，这样本程序就会产生异常，为了保证程序可以正常执行完毕，就需要通过
try-except语句进行异常的捕获与处理


"""
# coding : UTF-8
def main():					# 主函数
    try: 						# 捕获可能出现的异常
        raise NameError("NameError - 名称错误！") 		# 手工抛出异常类实例化对象
    except Exception as err: 				# 异常捕获
        print("【except】程序出现异常：%s" % err) 		# 输出异常信息
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
