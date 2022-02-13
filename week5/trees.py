import math

class Node:
    def __init__(self, key=0, parent = None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

def insert(root, node):
    if root.key > node.key:
        if root.left == None:
            root.left = node
            node.parent = root
        else:
            insert(root.left, node)
    else:
        if root.right == None:
            root.right = node
            node.parent = root
        else:
            insert(root.right, node)

#######################################################

def tree_size(root):
    if root is None:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)

def tree_max(root: Node):
    if root is None:
        return -math.inf
    return max(tree_max(root.right), tree_max(root.left), root.key)

def _check_BST(root):
    pass

def check_BST(root):
    return _check_BST(root)[0]

def _min_diff(root):
    pass

def min_diff(root):
    return _min_diff(root)[0]

#################################################

if __name__ == "__main__":
    T = Node(3)

    insert(T, Node(333))
    insert(T, Node(1))
    insert(T, Node(2))

    insert(T, Node(5))

    insert(T, Node(-17))

    print(tree_max(T))
    # should print True
#    print(check_BST(T))
    # should print 1
    #print(min_diff(T))
