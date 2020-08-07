"""
本程序为了进行列表对象的格式化处理，专门定义了一个MessageListFormat类，在该类中利用迭代的形式实现了对Member类中的__format__()
方法调用，并将若干次调用的结果拼凑为一个完整字符串并返回
"""
# coding : utf-8
class Message:
    def __init__(self, title, url): 			# 构造方法接收初始化参数
        self.__title = title				# 为属性赋值
        self.__url = url 				# 为属性赋值
    def __format__(self, format_spec): 			# 格式化字符串
        if format_spec == "":  			# 是否存在有格式化标记
            return str(self) 				# 不存在标记直接对象的字符串描述
        # 按照既定的标记“%title”与“%url”进行内容的字符串替换处理
        format_data = format_spec.replace("%title", self.__title).replace("%url", self.__url)
        return format_data				# 返回格式化后的字符串
    def __str__(self): 				# 覆写特殊方法
        return "名称：%s、网址：%s" % (self.__title, self.__url) # 返回对象信息
class MessageListFormat: 				# 定义格式化类
    def __init__(self,*msgs): 				# 构造方法
        self.msg_list = list(msgs) 			# 保存集合列表
    def __format__(self, format_spec): 			# 覆写特殊方法
        if format_spec == "": 				# 是否存在有格式化标记
            return str(self) 				# 不存在标记直接对象的字符串描述
        format_data = "\n".join("{:{fs}}".format(m, fs=format_spec) for m in self.msg_list)
        return format_data				# 返回格式化数据
def main():					# 主函数
    message_list = MessageListFormat(Message("沐言优拓", "www.yootk.com")) # 实例化对象
    message=Message("优拓讲师", "李兴华")		# 保存多个对象
    print("{info:%title：%url}".format(info=message_list)) 	# 定义格式化标记
    print("{info:%title：%url}".format(info=message))  # 定义格式化标记
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
