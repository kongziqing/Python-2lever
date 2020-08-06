"""
将对象的引用关联进一步扩展就可以实现更多的结构描述，在设计模式中有一种合成设计模式，此设计模式的核心思想为，通过不同的类实现
子结构定义，随后在一个副结构中将其整合，例如，现在要通过面向对象的设计思想描述一间教室的组或类结构，在教室中会有一张讲台，一块黑板，一张地图以及
若干套课桌椅。
本实例给出了一个伪代码的组成结构，实际上这也属于面向对象的基本设计思想，Python中提供的引用类型不仅仅是描述的内存操作形式，还包含了抽象与关联的设计想
"""

# coding : utf-8
class Blackboard: 					# 定义黑板类
    pass   					# 相关属性与方法略...
class Map: 					# 定义地图类
    pass   					# 相关属性与方法略...
class Platform: 					# 定义讲台类
    pass 						# 相关属性与方法略...
class DesksAndChairs: 				# 定义课桌椅类
    pass 						# 相关属性与方法略...
class Classroom: 					# 定义教室类
    def __init__(self): 				# 构造方法
        self.__platform = Platform()			# 实例化讲台类对象
        self.__board = Blackboard()			# 实例化黑板类对象
        self.__map = Map()				# 实例化地图类对象
        self.dc = []					# 实例化列表保存多套课桌椅信息
