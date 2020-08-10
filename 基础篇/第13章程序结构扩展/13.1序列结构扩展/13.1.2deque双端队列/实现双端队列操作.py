"""
双端对垒是一种线性存储结构，在双端队列的前端和后端都可以进行数据的存储与弹出操作，这样就可以方便的实现数据的FIFO（First Input First Output
,先进先出）与FILO（First Input Last Output，先进后出）
Python将双端队列（deque）定义在collections模块中，用户可以直接利用表中的方法进行队列操作

collections.deque操作方法
append(self,element)  向队列后端添加数据
appendleft(self,element)  向队列前端添加数据
clear(self)  清空队列数据
count(self,element) 获取指定元素在队列中的出现次数
pop(self) 从队列前端弹出数据
popleft(self) 从队列后端弹出数据
remove(self,element) 删除队列中的指定数据
reverse(self)  队列反转
"""

# coding : UTF-8
from collections import deque					# 模块导入
def main():						# 主函数
    info_deque = deque(("Hello", "Yootk"))			# 创建双端队列并保存数据
    info_deque.append("小李老师")				# 在队列后端添加数据
    info_deque.appendleft("沐言优拓")				# 在队列前端添加数据
    print("队列数据：%s，队列长度：%s" % (info_deque, info_deque.__len__()))
    print("从前端弹出数据：%s、从后端弹出数据：%s" % (info_deque.pop(), info_deque.popleft()))
    print("弹出数据后的队列长度：%s" % info_deque.__len__())
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
