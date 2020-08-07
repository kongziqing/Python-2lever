"""
属性拦截方法
1._setattr__(self,key,value)    设置属性时执行，key为属性名称，value为属性内容
2.__getattr__(self,item)         获取的属性不存在时执行，item为属性名称
3.__delattr__(self,item)          使用del关键字删除属性时触发，item为属性名称

本程序通过构造方法定义了content实例属性，当调用"实例化对象.属性"赋值时就会自动触发__setattr__()方法，在此方法中就可以
获得设置属性的名称以及内容，同时还需要将属性与内容保存在__dict__字典中才可以真正实现实例属性的创建，而在获取属性时，如果属性
不存在，则会自动触发__getattr__()方法，如果没有在子类中覆写此方法，那么久会出现AttributeError异常，而如果覆写了，就可以
由用户自定义属性不存在时的返回信息
"""
# coding : utf-8
class Message: 					# 默认object子类
    def __init__(self, content): 			# 构造方法定义属性
        self.__content = content 			# 保存属性内容
    def remove_content(self): 				# 删除属性
        del self.__content 				# 使用“del”关键字删除
    def get_content(self):  				# 获取属性内容
        return self.__content				# 返回属性内容
    def __setattr__(self, key, value): 			# 属性设置时拦截
        print("【setattr】key = %s、value = %s" % (key, value)) 	# 输出提示信息
        self.__dict__[key] = value			# 向“__dict__”中保存属性和数据
    def __getattr__(self, item): 			# 属性不存在时调用
        print("【getattr】item = %s" % item) 		# 提示信息
        return "%s属性不存在，返回Nothing" % item  	# 属性不存在时的返回值
    def __delattr__(self, item): 			# 属性删除
        print("【delattr】item = %s" % item) 		# 输出提示信息
        self.__dict__.pop(item) 			# 从字典中弹出数据
def main():					# 主函数
    msg = Message("www.yootk.com") 			# 实例化类对象
    print("【获取存在的属性】%s" % msg.get_content())	# 获取存在的属性内容
    print("【获取不存在的属性】%s" % msg.note) 		# 获取不存在的属性内容
    msg.remove_content()				# 删除属性
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
