"""
系统中的每一个进程都是一个独立的单元，拥有自己的资源信息，为了可以使不同进程之间进行数据交换就需要提供有通信管道
管道Pipe是系统进程通信的一个技术手段，开发者可以利用管道创建两个通信连接对象，这两个连接对象可以实现单端通信，
也可以实现双端通信，
进程通信管道的实现可以通过multiprocessing.Pipe类完成，也可以通过Pipe类提供的构造方法def Pipe(duplex)创建
接收管道（conn_recv）与发送管道（conn_send）两个管道连接对象，构造方法中参数duplex有两种取值
duplex = True:默认设置，允许两个连接进行双向通信
duplex = False：连接1（conn_recv）只允许接收数据，连接2（conn_send）只允许发送数据


本程序利用Pipe类的构造方法创建了两个连接通道对象，随后分别将这两个连接通道引用设置到不同的进程中，并利用send()与recv()两个方法就
可以实现数据的发送与接收处理

"""
import multiprocessing					# 模块导入
def send_data(conn, data): 					# 管道数据发送
    conn.send(["李兴华", "沐言优拓", data]) 			# 发送列表数据
def receive_data(conn): 					# 管道数据接收
    print("【数据接收】%s" % conn.recv())			# 输出接收到的数据
def main():						# 主函数
    conn_recv, conn_send = multiprocessing.Pipe()			# 产生两个连接对象
    # 创建两个子进程，分别设置好进程的处理函数与连接对象
    process_send = multiprocessing.Process(target=send_data, args=(conn_send, "www.yootk.com",))
    process_recv = multiprocessing.Process(target=receive_data, args=(conn_recv,))
    process_recv.start()					# 启动接收进程
    process_send.start()					# 启动发送进程
if __name__ == "__main__":					# 判断程序执行名称
    main()
