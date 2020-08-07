"""
为了清晰的描述抽象事物，一个累涨往往会提供大量的实例属性，同时通过封装来保护这些实例属性的操作安全，如果需要访问属性，
则通过对应的setter()与getter()方法进行操作，然而这种访问属性的方式在类中属性很多的情况下会非常麻烦，因为访问属性就需要采用
"对象.方法（）"的形式，而这种方式会弱化类中的属性操作，因为在更多的情况下，很多的开发者会认为，直接利用"对象。属性"的操作
方式要比通过方法调用更加方便，所以为了解决这一问题，Python提供了属性范围的简化支持，即利用@Property来完成

本程序通过属性装饰器为类中私有属性的操作方法进行了简化操作定义，这样在访问私有属性时将不需要通过"对象.set_xxx()"与“对象.get_xxx()”的形式访问，
简化了对象使用流程
"""
# coding : UTF-8
class Message: 				# 自定义Message类
    # 此时方法名称为info，而后会依据此方法名称定义“@info.setter”与“@info.deleter”，名称必须统一
    @property 				# 该操作为一个类实例属性
    def info(self): 				# 定义访问属性名称
        return self.__info			# 返回属性
    @info.setter 				# 属性内容设置
    def info(self,info): 			# 方法名称相同，但是表示设置属性内容
        self.__info = info			# 修改属性
    @info.deleter				# 属性删除
    def info(self): 				# 方法名称相同
        del self.__info			# 删除属性
def main():				# 主函数
    msg = Message()				# 实例化对象
    print("对象实例化后的属性列表内容：%s" % msg.__dict__)	# 提示信息
    msg.info = "www.yootk.com" 		# 调用“@info.setter”标记方法进行设置
    print(msg.info) 				# 获取属性内容，调用“@property”标记方法获取
    print("追加实例属性后的属性列表内容：%s" % msg.__dict__)	# 提示信息
    del msg.info                               	# 删除属性内容， 调用“@info.deleter”标记方法删除
    print("删除实例属性后的属性列表内容：%s" % msg.__dict__)	# 提示信息
if __name__ == "__main__":			# 判断执行名称
    main()					# 调用主函数

