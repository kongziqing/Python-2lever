"""
heapq堆是一种基于数据实现的完全二叉树，其最大的特点是其所存储的数据内容为有序存储，所以又可以将堆称为优先队列，
heapq实现的是最小堆
heapq的操作方法：
1.heapify(iterable)  向堆中追加一个可迭代对象，例如：列表
2.heappush(heap,element) 向堆中保存数据
3.heappop(heap)从堆中移除并弹出一个最小值
4.heappushpop(heap,ele) 先执行push操作，在执行pop操作
5.heapreplace(heap,ele) 先执行pop操作，再执行替换
6.nlargest(n,heap,key=fun) 获取前n个最大值
7.nsmallest(n,heap,key=fun) 获取前n个最小值
"""

# coding : UTF-8
import heapq						# 模块导入
def main():						# 主函数
    data = [6, 1, 3, 8, 9, 7] 					# 定义一个列表里面的数据无序存储
    heapq.heapify(data) 					# 基于迭代对象（iterable）创建堆
    heapq.heappush(data, 0) 					# 向堆中进行数据保存
    print("保存并弹出数据：%s" % heapq.heappushpop(data, 5)) 	# 弹出最小值
    print(heapq.nlargest(2,data)) 				# 获取堆中前2个最大数据
    print(heapq.nsmallest(3,data)) 				# 获取堆中前3个最小数据
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
