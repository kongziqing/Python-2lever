"""
本程序对调用拦截器的操作进行了名称的判断处理，如果调用的是content，那么久自定义一个字符串进行返回，如果是send，则更换一个可以
调用的other()方法返回，这样的处理就是的拦截器在开发中非常灵活
"""
# coding : utf-8
class Message: 					# 默认object子类
    def __getattribute__(self, item): 			# 覆写object类方法
        if item == "content": 				# 判断内容为content时的操作
            return "沐言优拓：www.yootk.com"		# 返回提示信息
        elif item == "send": 				# 判断名称
            return self.other				# 更换为其它方法
        else: 					# 其它操作不进行处理
            return object.__getattribute__(self, item) 	# 代码正常执行调用
    def send(self, info): 				# 定义类中的方法
        print("消息发送：%s" % info) 			# 输出提示信息
    def other(self,note): 				# 定义一个替代方法
        print("【替换方法-other】%s" % note) 		# 替代操作执行
def main():					# 输出提示信息
    msg = Message()					# 实例化类对象
    # 此时并没有为msg实例化对象动态配置实例属性，按照传统操作此时应该会出现“AttributeError”
    print(msg.content) 				# 获取属性触发“__getattribute__()”
    msg.send("www.jixianit.com") 			# 调用方法触发“__getattribute__()”
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
