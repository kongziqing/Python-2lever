"""
此时获取了2017年2月的日历信息，而在输出calendar对象时会自动调整格式，另外，需要注意的是，如果此时使用了calendar(2017)方法，
则会列出指定年份全部12个月的日历信息

提示：关于中文显示
如果开发者需要将日历的兴起数显示为中文，则可以利用locale模块设置文字编码

实例：设置文字编码
import locale
locale.setlocale(locale,LC_ALL,"zh_CN.UTF-8")
calendar.prmonth(2017,2)
此时就可以将日历显示为中文，但是中文显示时会由于文字长度问题导致数据显示错位
"""
# coding : UTF-8
import calendar					# 导入calendar模块
def main():					# 主函数
    cal = calendar.month(2017, 2) 			# 获取2017年2月的日历
    print(cal)  					# 日历显示
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
