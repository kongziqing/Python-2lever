"""
在类中定义的属性可以记录每一个对象的完整信息，但是在默认情况下，类中的全部属性可以在类
的外部直接通过对象进行调用，这样就会造成属性操作的不安全性，所以在类中定义的属性和方法就需要通过
封装进行私有化定义，
而封装也是面向对象编程中的第一大特性，如果要将属性封装，只需要在属性定义时使用“__属性名称”（两个下划线“_”）
定义即可，在类外部无法访问封装属性，此时可以在类中提供getter()和setter形式的间接访问

本程序在Member类中定义两个封装属性__name和__age,这样在进行封装属性访问时，就只能够通过定义好的
setter和getter方法间接访问，而此时如果直接在类外部通过对象进行私有属性访问，那么将出现AttributeError异常
"""
class Member:
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
def main():
    mem=Member()
    mem.set_name("kongziqing")
    mem.set_age(14)
    print("姓名：%s,年龄：%s"%(mem.get_name(),mem.get_age()))
if __name__ == '__main__':
    main()
