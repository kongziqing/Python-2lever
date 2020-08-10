"""
在本节第一个实例中，为了保证代码执行的正确性使用了一下的分支结构
if conn.build():#判断连接状态
    yield Message() #返回一个Message类实例
else：#连接失败
    yield None #返回空对象

该结构操作的特点在于：如果网络连接建立失败，为了避免程序出现RuntimeError异常，所以返回了一个空对象，如果用户已经明确
知道操作中可能产生此异常，并且不希望自己处理，那么久可以利用contextlib模块中提供的suppress类压制异常
"""
# coding : UTF-8
from contextlib import contextmanager,suppress		# 模块导入
class Message: 					# 消息发送类
    def send(self, info): 				# 消息发送
        print("【Message】消息发送：%s" % info) 		# 提示信息
@contextmanager 					# 将函数定义为上下文管理器
def message_wrap():					# 自定义函数
    class __Connect: 				# 定义一个连接工具类
        def build(self): 				# 创建连接
            print("【Connect】建立网络连接...") 		# 提示信息
            return False 				# 返回连接状态
        def close(self): 				# 关闭连接
            print("【Connect】关闭网络连接...") 		# 提示信息
    try: 						# 捕获可能产生的异常
        conn = __Connect()				# 实例化连接类对象
        if conn.build():				# 判断连接状态
            # 执行到yield代码时后续代码将不再执行，一直到with结构操作完毕后再继续执行
            yield Message()  				# 返回一个Message类实例
    finally:   					# 连接通道必须关闭
        conn.close()					# 调用类方法
def main():					# 主函数
    with suppress(RuntimeError, TypeError): 		# 可以压制多种异常
        with message_wrap() as msg:  			# 定义上下文管理
            msg.send("www.yootk.com")			# 调用Message类的send()方法
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
