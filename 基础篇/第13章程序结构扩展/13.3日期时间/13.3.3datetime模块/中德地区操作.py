"""
在日期时间定义之外还有一个最为重要的就是时区的概念，例如：德国是东一区，中国是东八区，德国比中国的时间慢7个小时，在Python中可
以通过datetime.tzinfo类来进行时区的设置，但是此类是一个在使用时需要定义的子类，并且在该子类中需要覆写tzname(),utcoffset(),dst()三个方法

本程序定义了一个表示时区的UTC子类，可以在该子类中设置时区偏移量，同时在datetime类中也提供有时区的转换操作
"""
# coding : UTF-8
from datetime import datetime, tzinfo, timedelta				# 导入模块相关类
class UTC(tzinfo): 							# 定义时区子类
    def __init__(self,offset = 0): 					# 设置市区偏移量
        self.__offset = offset						# 保存属性
    def tzname(self, dt): 						# 时区名称
        return "UTC +%s" % self._offset					# 获取市区名称
    def utcoffset(self, dt): 						# 时区偏移量
        return timedelta(hours=self.__offset) 				# 返回偏移量
    def dst(self, dt): 						# 获取夏时制
        return timedelta(hours=self.__offset) 				# 返回偏移量
def main():							# 主函数
    china_datetime = datetime(2017, 2, 17, 21, 15, 32, tzinfo=UTC(8)) 		# 中国时区
    germany_datetime = datetime(2017, 2, 17, 21, 15, 32, tzinfo=UTC(1)) 	# 德国时区
    print("北京日期时间：%s" % china_datetime) 				# 信息输出
    print("德国日期时间：%s" % germany_datetime) 				# 信息输出
    print("北京时间转为德国时间：%s" % (china_datetime.astimezone(UTC(1)))) 	# 时区转换
if __name__ == "__main__":						# 判断程序执行名称
    main()								# 调用主函数
