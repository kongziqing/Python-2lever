"""
单纯的代理设计模式中有一段代码时需要商榷的
food=FoodProxy(FoodReal())
在主函数中，用户需要明确地实例化子类对象才可以获得food实例化对象，但是从标准设计来讲，所有的子类对象应该对外部隐蔽，所以
对于此时的代码最好的修改方式是引入工厂设计模式
"""


class Food: 					# 定义食物标准
    def eat(self): 					# 定义公共业务方法
        pass					# 方法结构为空
class FoodReal(Food): 				# 定义真实业务实现子类
    def eat(self): 					# 方法覆写
        print("【FoodReal】享用丰盛的美食")		# 输出提示信息
class FoodProxy(Food): 				# 定义代理业务实现子类
    def __init__(self,food): 				# 保存真实业务对象
        self.__food = food				# 设置属性内容
    def prepare(self): 				# 真实业务执行前的准备
        print("【FoodProxy】准备做饭的食材。")		# 输出提示信息
    def eat(self): 					# 方法覆写
        self.prepare()				# 调用代理方法
        self.__food.eat()				# 调用真实业务方法
        self.clear()					# 调用代理方法
    def clear(self): 				# 真实业务执行后的处理方法
        print("【FoodProxy】收拾碗筷，打扫卫生。")		# 输出提示信息

def get_food_instance():
    return FoodProxy(FoodReal())
def main():					# 主函数
    food = get_food_instance()			# 获取指定类实例
    if food != None: 				# 判断是否有实例返回
        food.eat()					# 调用公共方法
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
