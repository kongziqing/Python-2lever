"""
函数重载是OOP的基本特性之一，名字相同但参数类型或个数不同时执行不同的函数，但因为Python是弱类型语言（不需要声明变量类型），
所以它不支持通过参数类型来支持重载，这是Python在3之前的不足之处，3.4之后，Python也提供重载机制：妆发（Dispatch）
"""

from functools import singledispatch

@singledispatch
def to_str(obj):
    print('%r'%(obj))

@to_str.register(int)
def _to_str(obj):
    print('Integer: %d'%(obj))

@to_str.register(str)
def _to_str(obj):
    print('String: %s'%(obj))

@to_str.register(list)
def _to_str(obj):
    print('List: %r'%(obj))


if __name__ == "__main__":
    to_str(1)
    to_str('hello')
    to_str(range(3))
    to_str(object)