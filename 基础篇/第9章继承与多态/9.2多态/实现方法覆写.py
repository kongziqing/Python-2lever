"""
本程序为Channel类定义了一个DatabaseChannel子类，并且在子类定义了与父类结构完全相同的build()方法，这样在利用子类实例化对象调用
build（）方法时所调用的就是被覆写过的方法
"""
# coding : utf-8
class Channel: 						# 定义父类
    def build(self): 					# 父类方法
        print("【Channel】通道连接...") 				# 输出提示信息
class DatabaseChannel(Channel): 				# 定义子类
    def build(self): 					# 方法覆写
        print("【DatabaseConnect】数据库通道连接...") 		# 输出提示信息
def main():						# 主函数
    channel = DatabaseChannel()				# 实例化子类对象
    channel.build()						# 调用被覆写过的方法
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
