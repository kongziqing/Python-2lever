class Person: 					# 定义Person父类
    def __init__(self): 				# 构造方法定义实例属性
        self.__name = None				# 属性默认值
        self.__age = 0				# 属性默认值
    def set_name(self, name): 				# 设置name属性内容
        self.__name = name				# 修改属性内容
    def set_age(self, age): 				# 设置age属性内容
        self.__age = age				# 修改属性内容
    def get_name(self): 				# 获取name属性内容
        return self.__name				# 返回属性内容
    def get_age(self): 				# 获取age属性内容
        return self.__age				# 返回属性内容
class Student(Person): 				# 定义Student类并继承Person父类
    pass 						# Student类中暂不定义任何内容
def main():					# 主函数
    stu = Student()					# 实例化子类对象
    stu.set_name("小李老师")				# 调用父类继承方法设置属性
    stu.set_age(18) 					# 调用父类继承方法设置属性
    print("姓名：%s、年龄：%s" % (stu.get_name(),stu.get_age()))	# 输出对象信息
if __name__ == "__main__":				# 判断程序执行名称
    main()
