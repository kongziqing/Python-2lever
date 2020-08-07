"""
Python中的字典数据可以按照key=value的形式进行数据的存储，随后可以动态的进行内容的设置、获取与删除操作，如果开发者有需要，也可以自定义类
的对象按照字典的形式进行操作，那么久要使用到一些特殊方法

1.__setitem__(self,key,value)  设置字典数据时触发
2.__getitem__(self,item)        根据key获取字典数据时触发
3.__delitem__(self,key)         使用del关键字删除字典数据时触发
4.__contains__(self,item)       判断指定的内容是否存在
5.__len__(self)     获取对象长度
"""
# coding : utf-8
class Message: 					# 默认object子类
    def __init__(self): 				# 构造方法
        self.__map = {}				# 定义一个空的字典
    def __setitem__(self, key, value): 			# 设置字典数据时触发
        print("【setitem】设置数据，key = %s、value = %s" % (key,value))
        self.__map[key] = value 			# 向字典保存数据
    def __getitem__(self, item): 			# 获取字典数据时触发
        print("【getitem】获取数据，item = %s" % item) 	# 输出提示信息
        return self.__map.get(item) 			# 从字典获取数据
    def __delitem__(self, key): 			# “del”删除数据时触发
        print("【delitem】删除数据，key = %s" % key) 	# 输出提示信息
        self.__map.pop(key) 				# 从字典中弹出数据
    def __len__(self): 				# 获取对象长度
        return len(self.__map) 			# 返回字典长度
def main():					# 主函数
    msg = Message()					# 实例化类对象，并可以按照字典模式操作
    msg["yootk"] = "www.yootk.com"			# 设置字典数据
    print("数据保存个数：%s" % len(msg)) 		# 获取数据长度
    print(msg["yootk"])				# 获取字典数据
    del msg["yootk"] 				# 删除字典数据
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
