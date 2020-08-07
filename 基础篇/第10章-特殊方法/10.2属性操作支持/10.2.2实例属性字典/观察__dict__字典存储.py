"""
Python最大的特点在于类中的每一个实例化对象都可以依据自己的需要动态的进行实例属性的配置，而所有的实例属性实际上都保存在了object类的
__dict__字典变量中。
本程序在Message类的构造方法中设置了一个note封装实例属性，随后在main()函数中设置了一个content实例属性，设置完成之后可以发现，所有
的属性内容都以字典的形式保存在了__dict__对象中。
"""
# coding : utf-8
class Message: 					# 默认object子类
    def __init__(self,note): 				# 构造方法设置属性
        self.__note = note 				# 操作实例属性
def main():					# 主函数
    msg = Message("沐言优拓")  			# 实例化类对象
    msg.content = "www.yootk.com" 			# 配置实例属性
    print(msg.__dict__) 				# 获取属性保存字典信息
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
