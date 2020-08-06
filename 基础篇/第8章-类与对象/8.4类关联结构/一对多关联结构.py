"""
在进行一对一类关联的基础上，结合序列结构的使用，就可以实现一对多的关联，
在进行类引用关联的操作之中，一对多的关联结构是一种较为常见的形式，例如，假设要描述这样一种关联，一个部门
有多为部门员工，为了方便部门管理，每个部门应设置一位正领导和一位副领导，
"""
# coding : utf-8
class Dept: 						# 定义部门类
    def __init__(self, **kwargs): 				# 构造方法
        self.__dname = kwargs.get("dname") 			# dname属性初始化
        self.__loc = kwargs.get("loc")				# loc属性初始化
        self.__emps = []					# 保存多个雇员
    def get_emps(self): 					# 获取所有员工信息
        return self.__emps					# 返回雇员列表引用
    def get_info(self): 					# 获取部门信息
        return "【Dept类】部门名称：%s，部门位置：%s" % (self.__dname, self.__loc)
    # setter、getter相关方法、略...
class Emp: 						# 雇员类
    def __init__(self, **kwargs): 				# 构造方法
        self.__ename = kwargs.get("ename")  			# ename属性初始化
        self.__sal = kwargs.get("sal") 				# sal属性初始化
    def set_mgr(self, mgr): 					# 设置员工对领导的引用
        self.__mgr = mgr					# 返回自身引用实例
    def get_mgr(self): 					# 获取领导
        if "_Emp__mgr" in dir(self): 				# 判断是否存在“__mgr”属性
            return self.__mgr  				# 存在返回对象
        else: 						# 没有领导
            return None					# 返回None
    def set_dept(self, dept): 					# 设置雇员所属部门
        self.__dept = dept					# 设置Dept引用实例
    def get_dept(self):  					# 获取雇员所属部门
        return self.__dept					# 获取Dept引用实例
    def get_info(self): 					# 获取雇员信息
        return "【Emp类】雇员姓名：%s，月薪：%s" % (self.__ename, self.__sal) # 返回对象信息
    # setter、getter相关方法、略...
def main():						# 主函数
    dept = Dept(dname="优拓教学部", loc="北京") 			# Dept对象实例化
    emp_a = Emp(ename="于顺", sal=35000.00) 			# Emp对象实例化
    emp_b = Emp(ename="陈浩东", sal=8500.00) 			# Emp对象实例化
    emp_c = Emp(ename="公孙夏丹", sal=7000.00) 			# Emp对象实例化
    emp_a.set_dept(dept) 					# 设置雇员与部门引用关联
    emp_b.set_dept(dept)  					# 设置雇员与部门引用关联
    emp_c.set_dept(dept)  					# 设置雇员与部门引用关联
    emp_b.set_mgr(emp_a)  					# 设置雇员与领导引用关联
    emp_c.set_mgr(emp_b)  					# 设置雇员与领导引用关联
    dept.get_emps().append(emp_a)  				# 设置部门雇员引用关联
    dept.get_emps().append(emp_b) 				# 设置部门雇员引用关联
    dept.get_emps().append(emp_c) 				# 设置部门雇员引用关联
    print(dept.get_info())    					# 输出部门信息
    for emp in dept.get_emps():				# 输出部门全部雇员信息
        print(emp.get_info())					# 雇员信息
        if emp.get_mgr() != None: 				# 如果该雇员有领导
            print("\t|- %s" % emp.get_mgr().get_info())             	# 输出领导信息
if __name__ == "__main__":				  	# 判断程序执行名称
    main()						  	# 调用主函数
