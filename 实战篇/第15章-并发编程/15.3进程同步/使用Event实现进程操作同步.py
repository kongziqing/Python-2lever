"""
Event是一种基于状态变量管理的进程同步机制，可以利用管理实现若干进程之间互相等待与唤醒的处理机制，本课程通过一个点餐的同步程序
讲解了Event操作的使用

multiprocessing.Event类提供了一个进程通信事件的管理操作，多个进程利用Event提供的阻塞标记实现等待与唤醒机制。

Event常用方法
def is_set(self)  获取当前阻塞状态
def wait(self,timeout=None) 进入阻塞状态，将阻塞标记设置为False，等待阻塞标记
在Event类同步处理时，多个进程将拥有同一个Event实例，当调用wait()方法时将进入到阻塞状态，
同时会将阻塞标记设置为False(待阻塞标记为True后才会解除阻塞状态)，与此同时，另外一个进程可以继续工作，
并且通过set()方法将阻塞标记设置为True，这样之前阻塞的进程也会继续执行

为了对不同的进程操作顺序进行限制，本程序使用了Event类来控制阻塞的开启与解除，需要注意的是，在进行阻塞解除时，为了防止有可能出现的阻塞
标记混乱，要调用clear()方法清空所有阻塞标记（将阻塞标记设置为False）
"""
import multiprocessing, time				# 模块导入
def restaurant_handle(event): 				# 餐厅
    print("1、【餐厅】为食客安排座位，并在一旁等待食客点餐... ")	# 提示信息
    time.sleep(1) 					# 延迟，模拟用户点餐时间
    event.set()					# 解除阻塞状态，阻塞标记设置为True
    event.clear()					# 清除所有的阻塞标记，防止出现标记错乱问题
    event.wait()					# 进入阻塞状态，阻塞标记为False
    print("3、【餐厅】厨师接到菜单，开始烹饪美食...") 	# 提示信息
    event.set()					# 解除阻塞状态，阻塞标记变为True
    event.clear()					# 清除所有的事件标记，防止出现标记错乱问题
def diners_handle(event): 				# 食客
    event.wait()					# 进入阻塞状态，阻塞标记为False
    print("2、【食客】食客看完菜单，选好了自己心仪的美食...")
    time.sleep(1) 					# 延迟，模拟餐厅烹饪时间
    event.set()					# 解除阻塞状态，阻塞标记变为True
    event.clear()					# 清除所有的阻塞标记，防止出现标记错乱问题
    event.wait()					# 进入阻塞状态，阻塞标记为False
    print("4、【食客】享用丰盛的美食...") 		# 提示信息
def main():					# 主函数
    event = multiprocessing.Event()			# 实例化Event类对象
    # 创建两个处理进程，并且这两个进程将操作同一个Event类实例
    restaurant_process = multiprocessing.Process(target=restaurant_handle,
        args=(event,), name="餐厅服务进程")		# 创建进程
    diners_process = multiprocessing.Process(target=diners_handle, args=(event,), name="食客进程")
    restaurant_process.start()				# 进程启动
    diners_process.start()				# 进程启动
if __name__ == "__main__":				# 判断程序执行名称
    main()

