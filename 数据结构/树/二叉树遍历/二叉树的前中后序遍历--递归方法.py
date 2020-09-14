'''
树的构建：
     3
  30     20
9   10  15    7
'''


class Tree():
    '树的构造'

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

#创建二叉树
def listCreatTree(root, llist, i):
    if i < len(llist):
        if llist[i] == '#':
            return None  ###这里的return很重要
        else:
            root = Tree(llist[i])
            # 往左递推
            root.left = listCreatTree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = listCreatTree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            return root  ###这里的return很重要
    return root



#----------------------------------------------------------------------------------
#使用递归方法进行前中后序遍历
class MyTree():
    '二叉树的实现'

    def __init__(self, base=0):
        self.base = base

    def _Empty(self):
        '判断是否为空树'
        if self.base == None:
            return True
        else:
            return False

    def front_search(self, tree_base):
        '前序遍历:根-左-右'
        if tree_base == None:
            return
        print(tree_base.data)
        self.front_search(tree_base.left)
        self.front_search(tree_base.right)

    def middle_search(self, tree_base):
        '中序遍历:左-根-右'
        if tree_base == None:
            return
        self.middle_search(tree_base.left)
        print(tree_base.data)
        self.middle_search(tree_base.right)

    def behind_search(self, tree_base):
        '后序遍历:左-右-根'
        if tree_base == None:
            return
        self.behind_search(tree_base.left)
        self.behind_search(tree_base.right)
        print(tree_base.data)


# test tree

#二叉树创建方法一
# tree1 = Tree(data=15)
# tree2 = Tree(data=7)
# tree3 = Tree(20, tree1, tree2)
# tree4 = Tree(data=9)
# tree5 = Tree(data=10)
# tree6 =Tree(30,tree4,tree5)
# base = Tree(3, tree6, tree3)


#二叉树创建方法二
#使用listCreatTree创建二叉树
llist = ['1', '2', '3', '#', '4', '5', '6']
base = listCreatTree(None, llist, 0)

btree = MyTree(base)
print('前序遍历:')
btree.front_search(btree.base)
print('中序遍历:')
btree.middle_search(btree.base)
print('后序遍历:')
btree.behind_search(btree.base)

#----------------------------------------------------------------
print('_____________________________________________________')
#--------------------------------------------------------------

#颜色标记法进行前中后序遍历
