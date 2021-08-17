class Node:
    def __init__(self ,data):
        self.left = None
        self.right = None
        self.data = data


def breadthfirst(root):
    if root is None:
        return
    my_list = []
    result=[]
    result.append(root.data)
    my_list.append(root)
    while(len(my_list) > 0):
        node = my_list.pop(0)
        if node.left is not None:
            my_list.append(node.left)
            result.append(node.left.data)
        if node.right is not None:
            my_list.append(node.right)
            result.append(node.right.data)
    return result        

            
root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.right = Node(9)
root.left.right.left = Node(5)
root.left.right.right = Node(11)
root.right.right.left = Node(4)

print(breadthfirst(root))

