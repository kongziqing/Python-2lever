"""
contextlib模块除了给了一个方便的上下文管理结构之外，还提供了一个closing类，该类在上下文操作完成后会自动欧诺个调用类中提供的close()方法
释放资源

本程序直接利用closing类实现了Connect连接类的操作管理，这样操作的方便之处在于只要类中提供了close()方法名称，开发者将不再需要显式调用此方法，而
会由closing类自动调用
"""
# coding : UTF-8
from contextlib import closing 		# 导入所需要模块中的类
class Connect: 				# 定义一个连接工具类
    def __init__(self): 			# 构造方法实现连接
        print("【Connect】建立网络连接...") 	# 输出提示信息
    def close(self): 			# 关闭连接
        print("【Connect】关闭网络连接...") 	# 输出提示信息
def main():				# 主函数
    with closing(Connect()) as conn: 		# 定义上下文管理
        print("消息发送：www.yootk.com")		# 消息发送
if __name__ == "__main__":			# 判断程序执行名称
    main()					# 调用主函数
