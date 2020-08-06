"""
使用传统网络模型进行I/O处理时，经常会出现由于传输文件过大而导致阻塞加大的问题，所以在twisted模块中提供了回调异步
Deferred模型
本程序通过一个简单的网络环境模拟了一次defer调用操作，通过程序的执行可以发现，在defer中需要注册成功与失败两个回调处理操作
。当work()方法执行完毕，会手工调用defer。callback（“finish”）方法，这样会触发设置的handle_success()方法的执行，同时
该方法还可以接收callback()传递的参数
"""
import twisted.internet.reactor 				# reactor处理
import twisted.internet.defer 				# defer处理
import time 						# 延迟处理
class DeferHandle: 					# 设置一个Defer处理类
    def __init__(self): 					# 提示信息
        self.defer = twisted.internet.defer.Deferred()		# 获取Defer对象
    def get_defer(self): 					# 获取Defferred对象
        return self.defer 					# 返回Defer对象实例
    def work(self): 					# 模拟网络下载
        print("模拟网络延迟操作，等待3秒时间。")			# 提示信息
        time.sleep(3) 					# 延迟3秒
        self.defer.callback("finish") 			# 模拟完成后手工触发
    def handle_success(self, result): 			# 处理完成回调
        print("处理完成，进行参数接收：%s" % result) 		# 提示信息
    def handle_error(self, d): 				# 处理失败回调
        print("程序出错：%s" % d) 				# 提示信息
def stop():						# 处理函数
    twisted.internet.reactor.stop()				# 结束reactor监听
    print("服务调用结束！")					# 提示信息
def main():						# 主函数
    defer_client = DeferHandle()				# 实例化Defer处理类
    twisted.internet.reactor.callWhenRunning(defer_client.work) 	#reactor调用耗时任务
    defer_client.get_defer().addCallback(defer_client.handle_success) # 添加处理回调
    defer_client.get_defer().addErrback(defer_client.handle_error) # 添加错误回调
    twisted.internet.reactor.callLater(5, stop) 		# 5秒后停止reactor循环
    twisted.internet.reactor.run()				# 运行程序
if __name__ == "__main__":     				# 判断执行名称
    main()
