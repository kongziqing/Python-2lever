# 以 f开头表示在字符串内支持大括号内的python 表达式
class StudentManager(object):
    #构建存储所用的列表
    def __init__(self):
        self.studentlist = []
    #一，程序入口函数，启动程序后执行的函数
    def run(self):
        #1.加载学员信息
        self.load_student()
        while True:
            #2.显示功能菜单
            self.show_menu()
            #3.用户输入功能序号
            menu_num = int(input('请输入您需要的功能序号'))
            #4.根据用户输入的功能序号执行不同的功能
            if menu_num==1:
                #添加学员
                self.add_student()
            elif menu_num==2:
                #删除学员
                self.del_student()
            elif menu_num ==3:
                #修改学员信息
                self.modify_student()
            elif menu_num ==4:
                #查询学员信息
                self.modify_student()
            elif menu_num == 5:
                #显示所有学员信息
                self.show_menu()
            elif menu_num == 6:
                #保存学员信息
                self.save_student()
            elif menu_num ==7:
                #退出系统
                break

    #二定义功能函数
    #2.1显示功能菜单
    @staticmethod
    def show_menu():
        print('请选择如下功能------------')
        print('')