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
        if node.left:
            my_list.append(node.left)
            result.append(node.left.data)
        if node.right:
            my_list.append(node.right)
            result.append(node.right.data)
    return result        

def count_file(root , root1):
    result = breadthfirst(root)
    final_result = result.count("file")
    result1 = breadthfirst(root1)
    final_result1 = result1.count("file")
    if final_result == final_result1:

     return True
    else:
        return False 


if __name__=="__main__":
            
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.right.right = Node("file")
    root.left.right.left = Node("file")
    root.left.right.right = Node("file")
    root.right.right.left = Node(4)
    
    root1 = Node(2)
    root1.left = Node(7)
    root1.right = Node(5)
    root1.left.left = Node(2)
    root1.left.right = Node(6)
    root1.right.right = Node("file")
    root1.left.right.left = Node("file")
    root1.left.right.right = Node("file")
    root1.right.right.left = Node(4)

    # print(breadthfirst(root))
    print(count_file(root , root1))
