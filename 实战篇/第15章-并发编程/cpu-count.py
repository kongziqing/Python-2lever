"""
获取本机CPU的内核数量
"""
from multiprocessing import cpu_count
print("CPU内核数量：%s"%cpu_count())#获取CPU个数