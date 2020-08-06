"""
内部类Connect类也可以在Message类的外部使用，
"""


class Message: 						# 自定义Message类
    def send(self, msg): 					# 消息发送
        conn = Message.Connect()				# 创建消息连接通道
        if conn.build():					# 连接消息通道
            print("【Message类】发送消息：%s" % msg) 		# 发送消息
            conn.close()					# 关闭消息通道
        else:  						# 通道创建失败
            print("〖ERROR〗消息通道创建失败，无法进行消息发送。") 	# 输出错误信息
    class Connect:  						# 通道管理工具类
        def build(self): 					# 通道连接
            print("【Connect类】建立消息发送通道。")		# 输出提示信息
            return True  					# 通道创建成功返回True
        def close(self): 					# 通道关闭
            print("【Connect类】关闭消息连接通道。")		# 输出提示信息
def main():				# 主函数
    con = Message.Connect()			# 外部实例化内部类对象
    print(con.build())			# 调用内部类方法
if __name__ == "__main__":			# 判断程序执行名称
    main()

"""
此时程序在Message类外部直接利用“外部类.内部类”的形式实例化了内部类对象，并直接调用了内部类的对象，如果开发者不希望内部类
被外部类所调用，则也可以使用__inner的形式进行内部类的封装定义，
class Message:
    class __Connect:
    .......
这样一来“__Connect”类只能够被Message所使用，外部无法调用
"""