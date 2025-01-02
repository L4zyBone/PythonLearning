# 1、完成二叉树的建树，前序，中序，后序，层序遍历
class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BinTree:
    def __init__(self):
        self.root = None
        self.bt_queue = []

    def add_node(self, node):
        self.bt_queue.append(node)
        if self.root is None:
            self.root = node
        else:
            if self.bt_queue[0].lchild is None:
                self.bt_queue[0].lchild = node
            else:
                self.bt_queue[0].rchild = node
                self.bt_queue.pop(0)


# 先序遍历二叉树
def pre_order(node):
    if node:
        print(node.elem, end=' ')
        pre_order(node.lchild)
        pre_order(node.rchild)


# 中序遍历
def mid_order(node):
    if node:
        mid_order(node.lchild)
        print(node.elem, end=' ')
        mid_order(node.rchild)


# 后序遍历
def last_order(node):
    if node:
        last_order(node.lchild)
        last_order(node.rchild)
        print(node.elem, end=' ')


# 层序遍历
def level_order(node):
    t_queue = [node]
    while t_queue:
        if t_queue[0].lchild:
            t_queue.append(t_queue[0].lchild)
        if t_queue[0].rchild:
            t_queue.append(t_queue[0].rchild)
        print(t_queue.pop(0).elem, end=' ')


if __name__ == '__main__':
    # 建树
    bi_tree = BinTree()
    # 插入结点
    for i in range(1, 11):
        new_node = Node(i)
        bi_tree.add_node(new_node)

# 先序遍历二叉树
pre_order(bi_tree.root)
print()
# 中序遍历二叉树
mid_order(bi_tree.root)
print()
# 后序遍历二叉树
last_order(bi_tree.root)
print()
# 层序遍历二叉树
level_order(bi_tree.root)
print()

# 2、完成sorted的练习
my_list = "This is a test string from Andrew".split()
print(my_list)
my_list.sort(key=lambda k: k.lower())
print(my_list)

student_tuples = [
    ('jane', 'B', 12),
    ('john', 'A', 15),
    ('dave', 'B', 10),
]

print(sorted(student_tuples, key=lambda k: k[0]))
student_tuples.sort(key=lambda k: k[1])
print(student_tuples)