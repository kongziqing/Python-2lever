"""
在进行异常处理是，如果直接输出异常对象，那么所能够得到的只是最为基础的异常信息，为了可以更加详细的获得异常的相关内容，Python
提供了一个traceback模块

此时的程序在出现异常之后会答应所有的异常信息以及出错的代码
"""
import traceback				# 导入模块
def main():				# 主函数
   try: 					# 捕获可能出现的异常
       b=1
       a=1/0
   except Exception as err: 			# 匹配任意异常
        print(traceback.format_exc())		# 获取异常详细信息
if __name__ == '__main__':
    main()