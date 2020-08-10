"""
枚举是一系列常量的集合，通常用于表示某些特定的有限对象的集合，例如，定义一周时间数信息（范围：一至周日），定义性别信息（范围：男，女）
、定义表示颜色基色信息（范围：红色，绿色，蓝色）。
本程序定义了一个描述一周时间数的week枚举类，同时在枚举类中定义了若干个枚举对象，这样当用户在使用week类时，就只能通过有限的几个对象进行操作。
"""

# coding : UTF-8
import enum 					# 导入枚举模块
@enum.unique					# 防止枚举内容重复
class Week(enum.Enum): 				# 定义枚举子类
    MONDAY = 0 					# 定义枚举项
    TUESDAY = 1 					# 定义枚举项
    WEDNESDAY = 2 					# 定义枚举项
    THURSDAY = 3 					# 定义枚举项
    FRIDAY = 4 					# 定义枚举项
    SATURDAY = 5 					# 定义枚举项
    SUNDAY = 6 					# 定义枚举项
def main():					# 主函数
    monday = Week.MONDAY				# 获取枚举对象
    print("枚举对象名称：%s、枚举对象内容：%s" %
	 (monday.name, monday.value)) 			# 信息提示
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
