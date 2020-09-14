#颜色标记法解决二叉树前中后序的遍历

"""
题目描述
给定一个二叉树，返回它的中序遍历
"""

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

class Solution:
    #中序遍历算法
    def inorderTraversal(self, root: Tree):
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.data)
        return res

    #前序遍历算法
    def front_search(self,root:Tree):
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GRAY, node))
            else:
                res.append(node.data)
        return res

    #后续遍历算法

    def behind_search(self,root:Tree):
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((GRAY, node))
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))

            else:
                res.append(node.data)
        return res








llist = ['1', '2', '3', '#', '4', '5', '6']
base = listCreatTree(None, llist, 0)


print('---------中序遍历------------------')
res=Solution().inorderTraversal(base)
print(res)

#---------------前序遍历------------
print('----------前序遍历------------')
res1=Solution().front_search(base)
print(res1)

#-------------后续遍历-------------
print('--------------后续遍历算法------------------')
res2=Solution().behind_search(base)
print(res2)