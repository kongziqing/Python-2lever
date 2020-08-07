"""
本程序完成了与之前相同的功能，但是从代码结构上来讲会更加清晰，这种基于Lambda形式实现的方法引用在以后的程序开发中也会经常出现
"""
class Message: 			# 自定义类
    def __init__(self,content): 	# 构造方法
        self.__content = content	# 属性赋值
    def __repr__(self) -> str: 	# 特殊方法
        return "【__str__()】%s" % self.__content	# 返回对象信息
def main():				# 主函数
    msg = Message("www.yootk.com") 		# 实例化类对象
    print(str(msg)) 				# 不使用str()函数也表示调用“__str__()”
    print(repr(msg)) 			# 必须使用repr()函数才可以调用“__repr__()”
if __name__ == "__main__":			# 判断程序执行名称
    main()