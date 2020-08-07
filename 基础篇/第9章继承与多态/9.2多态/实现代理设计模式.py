"""
代理设计是指通过一个代理主题来操作真实业务主题，真实主题执行具体的业务标准，而代理主题负责其他相关的处理。即。食客饿了的时候准备去餐厅
吃饭，"吃饭"即为真实主题，而餐厅为食客“吃饭”的业务做各种辅助操作（如购买食材，处理食材，烹制美食，收拾餐具），即为代理主题，而食客
只负责关键的一步"吃"就可以了

本陈旭为一个Food父类定义了两个子类，真实主题类（FoodReal）和代理主题类（FoodProxy），真实主题类只有在代理类提供支持的情况下才可以
正常完成核心业务，但是对于主函数（客户端）而言，其所关注的只有Food类定义业务标准，而并不关注具体使用哪一个子类。
"""
# coding : utf-8
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
def main():					# 主函数
    food = FoodProxy(FoodReal())			# 获取指定类实例
    if food != None: 				# 判断是否有实例返回
        food.eat()					# 调用公共方法
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
