"""
为了方便开发，Python已经提供了大量的异常类，但是这些异常类在实际的工作中往往并不完全满足需求，例如，假设要定义一个吃饭的操作，
有可能会产生”吃撑扎渡“（BombException）的异常，而Python并不会提供该类异常，这就需要开发者根据业务需要自定义异常类，自定义异常类
可以通过集成Exception父类来实现

本程序涉及了一个自定义的异常类型，当满足指定条件时就可以手工抛出异常，利用自定义异常机制可以更加清晰，准确地描述当前的业务场景，
所以实际项目开发都会根据自身的业务需求自定义大量的异常类型。
"""
# coding : UTF-8
class BombException(Exception): 				# 自定义异常类
    def __init__(self, msg = "BombException"): 			# 接收提示信息
        self.msg = msg					# 保存提示信息
    def __str__(self):    					# 返回对象信息
        return self.msg					# 返回属性内容
class Food: 						# 自定义业务类
    @staticmethod						# 减少实例化对象个数使用静态装饰
    def eat(num): 						# 吃饭方法
        if num > 999: 					# 异常触发条件
            raise BombException("吃太多了，肚子进入爆炸倒计时...") 	# 向上抛出异常
        else: 						# 条件不满足
            print("敞开吃，哥有万人羡慕的身材，吃多少都不胖...") 	# 输出提示信息
def main():						# 主函数
    try: 							# 捕获可能出现的异常
        Food.eat(1000) 					# 调用Food.eat()并传入参数
    except BombException as err: 				# 异常处理
        print("【except】异常处理：%s" % err) 			# 输出提示信息
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
