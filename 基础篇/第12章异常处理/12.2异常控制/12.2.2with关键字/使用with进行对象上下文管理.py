"""
在程序进行资源访问的过程中，为了保证资源不被浪费，往往需要及时释放资源，以客户端向服务端发送信息为例，在消息发送前应该建立服务器连接同奥，
而消息发送完毕不管是否产生异常都应该自动地关闭服务器连接通道，此时的程序逻辑如果使用传统的异常处理语句进行编写则会非常繁琐，为了
解决这一问题，Python提供了with语句，以实现对象的上下文管理。

程序利用with结构可以方便的执行一些程序功能的初期操作与收尾工作，这就需要两个特殊方法的支持，
__enter__(self)  当with语句开始执行时触发此方法执行
__exit__(self，type,value,trace)  当with语句结束后触发此方法执行，该方法又三个参数，作用如下：
*type :如果抛出异常，此处用于接收异常类型
*value:若果抛出异常，此处用于接收异常内容
*trace：如果抛出异常，此处显示异常所在的位置

本程序通过with定义了一个message对象，这样在该对象调用类中的方法前会自动调用Message类中定义的__enter__()方法进行资源初始化，
当with语句中的全部代码执行完毕后者执行方法产生异常后将自动调用__exit__()方法释放资源
"""
# coding : UTF-8
class Message: 						# 自定义Message类
    class __Connect: 					# 定义网络连接内部类
        def build(self): 					# 通道连接
            print("【Connect类】建立消息发送通道。")		# 输出提示信息
            return True 					# 通道创建成功返回True
        def close(self): 					# 通道关闭
            print("【Connect类】关闭消息连接通道。")		# 输出提示信息
    def send(self, msg):  					# 消息发送
        print("【Message类】发送消息：%s" % msg) 			# 发送消息
    def __enter__(self): 					# with进入时执行
        print("【enter】with语句开始执行")			# 输出提示信息
        self.__conn = Message.__Connect()			# 创建消息连接通道
        if not self.__conn.build():				# 判断连接是否建立成功
            print("〖ERROR〗消息通道创建失败，无法进行消息发送。")	# 输出错误信息
        return self 						# 需要返回当前对象
    def __exit__(self, type, value, trace): 			# with退出时执行
        print("【exit】with语句执行完毕")			# 输出提示信息
        self.__conn.close()					# 释放资源
def main():						# 主函数
    with Message() as message: 				# 使用with结构
        message.send("www.yootk.com") 				# 直接调用类方法
        message.send("www.yootk.com")  				# 直接调用类方法
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数


