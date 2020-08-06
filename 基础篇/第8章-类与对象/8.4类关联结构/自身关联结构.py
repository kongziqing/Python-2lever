"""
在进行类关联描述的过程中，除了可以关联其他类之外，也可以实现自身的关联操作，例如
，现在假设一个人会有一辆车，那么每个人可能还有自己的多为后代，而每位后代也有可能有一辆车，这时就可以利用自身关联的形式描述人员后代的关系，
而多位后代可以利用列表来描述，

由于一个人的后代可能会有零个或多个，为了方便进行多个本类对象的存储，本实例使用一个列表结构定义了children实例属性，并依据既定的信息实现
了引用的关联定义
"""


# coding : utf-8
class Member: 					# 人员信息类
    def __init__(self, **kwargs): 			# 构造方法
        self.__name = kwargs.get("name") 		# name属性初始化
        self.__age = kwargs.get("age")			# age属性初始化
        self.__children = []				# 定义空列表
    def get_children(self): 				# 返回一个人的全部后代
        return self.__children				# 返回列表引用
    def set_car(self,car): 				# 设置Car类引用
        self.__car = car				# 设置Car引用实例
    def get_car(self): 				# 获取Car类引用
        return self.__car				# 返回Car引用实例
    def get_info(self): 				# 获取人员信息
        return "【Member类】姓名：%s，年龄：%d" % (self.__name,self.__age) # 返回对象信息
    # setter、getter相关方法、略...
class Car: 					# 汽车信息
    def __init__(self, **kwargs): 			# 构造方法
        self.__brand = kwargs.get("brand")		# brand属性初始化
        self.__price = kwargs.get("price") 		# price属性初始化
    def set_member(self,member): 			# 设置Member类引用
        self.__member = member				# 设置Member引用实例
    def get_member(self): 				# 获取Member类引用
        return self.__member				# 返回Member引用实例
    def get_info(self): 				# 获取汽车信息
        return "【Car类】汽车品牌：%s，汽车价格：%s" % (self.__brand,self.__price) # 返回对象信息
def main():
    mem = Member(name="陈浩东",age=50) 			# 实例化Member类对象
    chd_a = Member(name="于顺",age=48) 			# 实例化Member类对象
    chd_b = Member(name="公孙夏丹",age=38) 		# 实例化Member类对象
    car_a = Car(brand="奔驰G50",price=1588800.00) 		# 实例化Car类对象
    car_b = Car(brand="碰碰车",price=2800.81) 		# 实例化Car类对象
    car_c = Car(brand="公交车",price=1308800.00) 		# 实例化Car类对象
    mem.set_car(car_a) 				# 一个人有一辆车
    chd_a.set_car(car_b) 				# 一个人有一辆车
    chd_b.set_car(car_c) 				# 一个人有一辆车
    car_a.set_member(mem) 				# 一辆车属于一个人
    car_b.set_member(chd_a) 				# 一辆车属于一个人
    car_c.set_member(chd_b) 				# 一辆车属于一个人
    mem.get_children().append(chd_a) 			# 追加父子关系
    mem.get_children().append(chd_b) 			# 追加父子关系
    print(mem.get_info())				# 输出父亲信息
    print("\t|- %s" % mem.get_car().get_info())		# 输出自己拥有的汽车信息
    for child in mem.get_children():			# 迭代后代信息
        print(child.get_info())			# 输出后代信息
        print("\t|- %s" % child.get_car().get_info())	# 输出后代拥有的汽车信息
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
