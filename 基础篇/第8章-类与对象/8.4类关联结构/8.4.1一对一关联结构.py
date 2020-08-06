"""
本程序定义了两个程序类，Memeber(描述人的信息)和Car（描述车的信息），并且在这两个类的内部分别设置一个自定义
的引用类型（Member类提供有car实例属性，Car类提供有member实例属性，）用于描述两个类之间的引用练习，在main()函数
操作中首先根据两个类的关系设置了引用关系，随后就可以根据引用关系依据某个类对象获取相应的信息
"""
# coding : utf-8
class Member: 					# 人员信息类
    def __init__(self, **kwargs): 			# 构造方法
        self.__name = kwargs.get("name")			# name属性初始化
        self.__age = kwargs.get("age")			# age属性初始化
    def set_car(self,car): 				# 设置Car类引用
        self.__car = car				# 接收Car引用实例
    def get_car(self): 				# 获取Car类引用
        return self.__car				# 返回Car引用实例
    def get_info(self): 				# 获取人员信息
        return "【Member类】姓名：%s，年龄：%d" % (self.__name,self.__age) # 返回对象信息
    # setter、getter相关方法、略...
class Car:  					# 汽车信息
    def __init__(self, **kwargs): 			# 构造方法
        self.__brand = kwargs.get("brand")		# brand属性初始化
        self.__price = kwargs.get("price") 		# price属性初始化
    def set_member(self,member):  			# 设置Member类引用
        self.__member = member				# 接收Member引用实例
    def get_member(self):  				# 获取Member类引用
        return self.__member				# 返回Member引用实例
    def get_info(self): 				# 获取汽车信息
        return "【Car类】汽车品牌：%s，汽车价格：%s" % (self.__brand,self.__price) # 返回对象信息
    # setter、getter相关方法、略...
def main():
    mem = Member(name="陈浩东",age=50) 			# 实例化Member类对象
    car = Car(brand="奔驰G50",price=1588800.00) 		# 实例化Car类对象
    mem.set_car(car) 				# 一个人有一辆车
    car.set_member(mem)  				# 一辆车属于一个人
    print(mem.get_car().get_info())			# 通过人获取车的信息
    print(car.get_member().get_info())			# 通过车获取人的信息
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
