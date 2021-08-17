from trees.tree_breadth_first import *

def test_tree_breadth_first():
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.right.right = Node(9)
    root.left.right.left = Node(5)
    root.left.right.right = Node(11)
    root.right.right.left = Node(4)

    assert breadthfirst(root)==[2, 7, 5, 2, 6, 9, 5, 11, 4]