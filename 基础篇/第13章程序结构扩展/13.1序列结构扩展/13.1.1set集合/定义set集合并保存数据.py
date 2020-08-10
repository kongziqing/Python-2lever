"""
set是Python中提供的一个集合定义类，其最大的特点是不保存重复数据，使用该类可以实现对数据的动态存储，由于其不保存数据的存储索引，
所以set集合中保存的数据是无序的，set集合中的常用操作方法如表：
add(self,element)   想集合追加数据
clear(self) 清空集合数据
copy(self)  集合浅拷贝
difference(self,t)  计算两个集合的差集，等价于s-t
intersection(self,t)    计算两个集合的交际，等价于s&t
symmetric_difference(self,t)    计算两个集合的对称差集，等价于s^t
union(self,t)   计算两个集合的并集，等价于s|t
discard(self,element)   如果元素存在，则删除
update(self,seq)    更新集合数据
remove(self,element) 从集合删除元素
pop(self) 从集合弹出一个元素

在set集合创建时，可以直接将所有要保存的数据定义在序列中，也可以创建一个空的set集合并利用add()方法动态地添加数据
本程序通过set类的构造方法将一个序列数据转为set集合，通过输出的结果可以发现，重复的数据内容自动被删除，同时采用无序的方式进行数据存储
"""
# coding : UTF-8
def main():						# 主函数
    info_set = set(["hello", "yootk", "Yootk", "hello", "小李老师"]) 	# 定义set集合，并保存数据
    info_set.add("www.yootk.com") 				# 追加数据
    print(info_set) 						# 直接输出数据
if __name__ == "__main__":					# 判断程序执行名称
    main()							# 调用主函数
