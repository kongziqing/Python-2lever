"""
为了方便上下文管理，Python提供了with结构，但是传统的with结构是基于类的定义形式，并且需要在类中提供__enter__()和__exit__()两个方特殊
方法才可以使用，为了简化这一结构(不强制性使用__enter__()和__exit__()两个特殊方法)，Python从Python2.5开始提供了contextlib模块，
随后可以使用@contextmangager装饰器将一个函数作为上下文管理器

本程序针对message_wrap()函数实现了一个上下文管理结构，当连接创建时将通过yield返回一个Message类的实例，由于存在yield关键字，所以当所有
消息发送完毕才会继续执行message_wrap()函数的后续部分
"""
# coding : UTF-8
from contextlib import contextmanager			# 模块导入
class Message: 					# 消息发送类
    def send(self, info): 				# 消息发送
        print("【Message】消息发送：%s" % info) 		# 提示信息
@contextmanager					# 将函数定义为上下文管理器
def message_wrap():					# 上下文管理装饰器
    class __Connect: 				# 定义一个连接工具类
        def build(self): 				# 创建连接
            print("【Connect】建立网络连接...") 		# 提示信息
            return True				# 返回连接状态
        def close(self): 				# 关闭连接
            print("【Connect】关闭网络连接...") 		# 提示信息
    try: 						# 捕获可能产生的异常
        conn = __Connect()				# 实例化连接类对象
        if conn.build():				# 判断连接状态
            # 执行到yield代码时后续代码将不再执行，一直到with结构操作完毕后再继续执行
            yield Message()  				# 返回一个Message类实例
        else: 					# 连接失败
            yield None				# 返回空对象
    except: 					# 异常处理
        print("【except】连接出现异常...") 		# 提示信息
    finally: 					# 连接通道必须关闭
        conn.close()					# 释放资源
def main():					# 主函数
    with message_wrap() as msg: 			# 定义上下文管理
        msg.send("www.yootk.com")			# 调用Message类的send()方法
if __name__ == "__main__":				# 判断程序执行名称
    main()						# 调用主函数
