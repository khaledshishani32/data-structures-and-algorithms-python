

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def display(self):
        output = []
  
        current = self.head
        while current:
            output.append(current.value)
            current = current.next
        return output


class HashTable:

    def __init__(self, size=521) -> None:
        self.bucket = [None] * size
        self.size = size

    def add(self, key, value):
        index = self.hash(key)

        if self.bucket[index] is None:
            self.bucket[index] = LinkedList()
        self.bucket[index].add([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.bucket[index] is None:
            return None
        else:
            current = self.bucket[index].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next

    def contains(self, key):
        index = self.hash(key)
        if self.bucket[index] == None:
            return False
        else:
            current = self.bucket[index].head
            while current:
                if current.value[0] == key:
                    return True
                else:
                    return False

    def hash(self, key):
        value = 0
        for character in key:
            value += ord(character)
        idx = value * 7 % self.size
        return idx



class Tree_node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

           

class B_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Tree_node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._insert(value, node.left)
            else:
                node.left = Tree_node(value)
        else:
            if node.right is not None:
                self._insert(value, node.right)
            else:
                node.right = Tree_node(value)    


def intersection(tree1,tree2):
    result=[]
    hashtable=HashTable(1024)

    if tree1.root is None or tree2.root is None:
        return None

    def preorder(node):
        if hashtable.contains(str(node.value)):
            nonlocal result
            result+=[node.value]
        else:
            hashtable.add(str(node.value),True)
        
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)
    preorder(tree1.root)
    preorder(tree2.root)

    return result



if __name__ == "__main__":
 
    tree1 = B_tree()
    tree1.insert(10)
    tree1.insert(20)
    tree1.insert(30)
    tree1.insert(40)
    tree1.insert(50)
    tree1.insert(600)
    
    print("=========================")
    tree2 = B_tree()
    tree2.insert(10)
    tree2.insert(20)
    tree2.insert(30)
    tree2.insert(40)
    tree2.insert(50)
    tree2.insert(7)
   
    print("=========================")
    print(intersection(tree1 , tree2))

 
    