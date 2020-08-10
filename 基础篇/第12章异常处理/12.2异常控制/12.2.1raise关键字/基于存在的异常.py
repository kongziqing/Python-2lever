"""
在使用raise关键字抛出异常时也可以利用基于一个已经存在的异常，此时会自动将该异常附加到引发异常的__cause__属性中

本程序在fun()函数中进行异常处理时，根据已经产生的NameError实例化对象附加了一个新的TypeError实例化对象，
这样就可以在main()函数进行异常处理时通过__cause__获取异常来源信息

提示：不附加__cause__属性
如果现在不希望通过raise抛出的异常附加到__cause__中，则可以使用None定义来源
raise TypeError(“TypeError-类型错误！”) from None
此时的程序抛出的TypeError异常不会将其产生来源附加到__cause__属性中
"""

# coding : UTF-8
def fun():						# 自定义函数
    try: 						# 捕获可能产生的异常
        raise NameError("NameError - 名称错误！") 		# 手工抛出异常类实例化对象
    except Exception as err: 				# 异常捕获
        print("【except-fun】程序出现异常：%s" % err) 	# 输出异常信息
        raise TypeError("TypeError - 类型错误！") from err	# 依据NameError实例抛出新的异常
def main():					# 主函数
    try: 						# 捕获可能产生的异常
        fun()					# 函数调用
    except Exception as err: 				# 异常捕获
        print("【except-main】程序出现异常：%s、cause = %s" %
	 	 (err, err.__cause__))		# 输出异常信息
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
