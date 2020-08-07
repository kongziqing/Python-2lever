"""
在面向对象设计中，父类的主要功能是进行各个子类操作方法标准的定义，所以不管何种子类，只要按照父类中的方法要求覆写了方法，那么就
可以通过父类对象的形式来进行表示 ，也就是说，此时调用处需要关心的父类实例，而并不需要关心子类的实例，为了达到这一目的，项目开发中
可以引入工程设计模式来隐藏子类。

本程序通过get_food_istance()工厂函数获取了Food类的实例化对象，利用这样的结构，主函数就可以在不清楚子类的情况下获取类的实例化对象
并依据Food父类定义的方法标准执行程序。

提示：系统内置工厂函数
在面向对象设计中，工厂函数的主要目的是获取指定的对象实例，在之前所学习过的int(),str(),float(),tuple()等函数实际上都属于内置的
工厂函数，通过函数传递若干参数后就可以获取指定类型的实例化对象。
"""
# coding : utf-8
class Food: 					# 定义食物标准
    def eat(self): 					# 定义公共方法
        pass					# 方法结构为空
class Bread(Food): 					# 定义面包子类
    def eat(self): 					# 覆写方法
        print("【Bread】吃面包")			# 输出提示信息
class Milk(Food): 					# 定义牛奶子类
    def eat(self): 					# 覆写方法
        print("【Milk】喝牛奶")			# 输出提示信息
"""
获取Food接口实例
@:param cls 要获取实例的名称标记
"""
def get_food_instance(cls): 				# 工厂函数
    if cls == "bread": 				# “bread”代表Bread子类
        return Bread()				# 返回Bread子类实例
    elif cls == "milk": 				# “milk”代表Milk子类
        return Milk()				# 返回Milk子类实例
    else: 						# 没有匹配返回None
        return None					# 返回None
def main():					# 主函数
    food = get_food_instance("bread")  			# 获取指定类实例
    if food != None: 				# 判断是否有实例返回
        food.eat()					# 调用公共方法
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
