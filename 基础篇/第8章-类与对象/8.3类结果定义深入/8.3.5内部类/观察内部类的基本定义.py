"""
本程序在Message类中定义了一个Connect内部类，此类的主要功能就是负责消息发送通道的连接与关闭，在使用Message类中的send()方法发送
消息时会根据Connect.build()连接情况的不同进行不同的处理。
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
def main():						# 主函数
    message = Message()					# 实例化Message类对象
    message.send("www.yootk.com") 				# 发送消息内容
if __name__ == "__main__":					# 判断程序执行名称
    main()
