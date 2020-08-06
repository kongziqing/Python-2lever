"""
获取内存信息
此时获取的内存数据信息都以字节的形式返回，例如：当前的总内存为34276925440字节，那么通过计算
(34276925440/1024/1024/1024)可以得出32GB物理内存，通过同样的方式可以输出交换空间（可以简单的理解为
Windows虚拟内存）的内存总量为36GB
"""
import psutil   						# pip install psutil
def main():						# 主函数
    print("【物理内存】内存总量：%d、可用内存：%d、已使用内存：%d、空闲内存：%d" % (
	psutil.virtual_memory().total, psutil.virtual_memory().available,
	psutil.virtual_memory().used, psutil.virtual_memory().free)) # 信息输出
    print("【swap内存】内存总量：%d、已使用内存：%d、空闲内存：%d" % (
	psutil.swap_memory().total, psutil.swap_memory().used,
	psutil.swap_memory().free)) 			# 信息输出
if __name__ == "__main__":					# 判断程序执行名称
    main()
