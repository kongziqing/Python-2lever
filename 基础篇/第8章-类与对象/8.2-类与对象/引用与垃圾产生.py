"""
在Python中每一块内存都可以被不同的对象同时指向，这些对象可以同时对内存中的数据进行操作
，但是每一个对象只允许保存一个引用地址，如果现在引用地址发生了改变，则就会断开已经引用的内存空间并指向
新的内存空间

注意;减少垃圾产生
虽然Python针对垃圾空间提供有GC（Garbage Collection,垃圾回收）机制，但是在代码编写中，如果产生了过多
的垃圾，则会影响程序的性能，所以开发人员编写代码的过程中，应该尽量减少无用对象的产生，以减少垃圾的产生。
"""
class Member: 					# 自定义Member类
    def set_info(self,name,age): 			# 设置属性方法
        self.name = name				# 设置name属性内容
        self.age = age				# 设置age属性内容
    def get_info(self): 				# 获取对象信息
        return "姓名：%s，年龄：%d" % (self.name,self.age) 	# 以字符串形式返回属性内容
def main():					# 主函数
    mem_a = Member()					# 实例化Member类对象
    mem_b = Member()					# 实例化Member类对象
    mem_a.set_info("小李老师",18) 			# 设置实例属性内容
    mem_b.set_info("优拓教育",5) 			# 设置实例属性内容
    print("【引用传递前】mem_a对象地址：%d、mem_b对象地址：%d" % (id(mem_a), id(mem_b)))
    mem_a = mem_b 					# 引用传递
    print(mem_a.get_info())				# 输出实例属性信息
    print("【引用传递后】mem_a对象地址：%d、mem_b对象地址：%d" % (id(mem_a), id(mem_b)))
if __name__ == "__main__":				# 判断程序执行名称
    main()
