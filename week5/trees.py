import math


class Node:
    def __init__(self, key=0, parent=None):
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


def _check_BST(root: Node):
    if root is None:
        return True, math.inf, -math.inf
    is_left_bst, min_left_bst, max_left_bst = _check_BST(root.left)
    is_right_bst, min_right_bst, max_right_bst = _check_BST(root.right)
    minimum = min(root.key, min_left_bst, min_right_bst)
    maximum = max(root.key, max_left_bst, max_right_bst)
    if is_left_bst == False or is_right_bst == False:
        return False, minimum, maximum

    if max_left_bst <= root.key <= min_right_bst:
        return True, minimum, maximum

    return False, minimum, maximum


def check_BST(root):
    return _check_BST(root)[0]


def _min_diff(root):
    if root is None:
        return True, math.inf, -math.inf
    left_diff, min_left_bst, max_left_bst = _check_BST(root.left)
    right_diff, min_right_bst, max_right_bst = _check_BST(root.right)
    minimum = min(root.key, min_left_bst)
    maximum = max(root.key, max_right_bst)
    return min(left_diff,right_diff, root.key - max_left_bst, -root.key + min_right_bst), minimum, maximum


def min_diff(root):
    return _min_diff(root)[0]


def _count_distinct(root):
    if root is None:
        return set()

    right_subtree = _count_distinct(root.right)
    left_subtree = _count_distinct(root.left)

    unique_keys = right_subtree.union(left_subtree)
    unique_keys.add(root.key)
    return unique_keys


def count_distinct(root):
    return len(_count_distinct(root))

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
    print(count_distinct(T))
# should print 1
# print(min_diff(T))
