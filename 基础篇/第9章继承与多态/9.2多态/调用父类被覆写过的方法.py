"""
本程序子类覆写了build（）方法，这样在子类中只能通过super().build()调用父类中已经被覆写过的方法
"""
# coding : utf-8
class Channel: 					# 定义父类
    def build(self): 				# 父类方法
        print("【Channel】通道连接...") 			# 输出提示信息
class DatabaseChannel(Channel): 			# 定义子类
    def build(self): 				# 方法覆写
        super().build()				# 调用父类被覆写过的方法
        print("【DatabaseConnect】数据库通道连接...") 	# 输出提示信息
def main():					# 主函数
    channel = DatabaseChannel()			# 实例化子类对象
    channel.build()  				# 调用被覆写过的方法
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
