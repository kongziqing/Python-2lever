"""
为了进行字符串格式化处理，Python专门提供了各种格式化的标记，对于用户而言，也可以定义属于自己的格式化标记，
此时就需要在类中覆写__format__()方法
"""
# coding : utf-8
class Message: 					# object子类
    def __init__(self, title, url): 			# 构造方法接收初始化参数
        self.__title = title				# 为属性赋值
        self.__url = url				# 为属性赋值
    def __format__(self, format_spec): 			# 格式化字符串
        if format_spec == "": 				# 是否存在有格式化标记
            return str(self) 				# 不存在标记直接对象的字符串描述
        # 按照既定的标记“%title”与“%url”进行内容的字符串替换处理
        format_data = format_spec.replace("%title", self.__title).replace("%url", self.__url)
        return format_data				# 返回格式化后的字符串
    def __str__(self): 				# 获取对象信息
        return "名称：%s、网址：%s" % (self.__title, self.__url) # 返回对象内容
def main():					# 主函数
    msg = Message("优拓软件学院","www.yootk.com") 		# 实例化对象
    print("{}".format(msg)) 				# 未指定格式化字符串，返回对象的字符串表示
    print("{info:%title：%url}".format(info=msg)) 		# 定义格式化标记
    print(format(msg, "%title：%url"))			# 通过format()函数格式化
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
