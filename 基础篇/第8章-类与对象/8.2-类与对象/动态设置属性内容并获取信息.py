class Member: 					# 自定义Member类
    def get_info(self): 				# 定义方法
        return "姓名：%s，年龄：%d" % (self.name,self.age) 	# 返回信息
def main():					# 主函数
    mem = Member()					# 实例化Member类对象
    mem.name = "小李老师"				# 定义实例属性并设置内容
    mem.age = 18 					# 定义实例属性并设置内容
    print(mem.get_info())				# 调用类中方法获取信息
if __name__ == "__main__":				# 判断程序执行名称
    main()
