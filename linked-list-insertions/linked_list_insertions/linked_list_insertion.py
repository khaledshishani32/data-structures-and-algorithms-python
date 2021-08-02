class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    inestance=[]
    def __init__(self):
        self.head = None
    def insert(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            return self.head.value
        else:
            current = self.head
            self.head = node
            self.head.next = current
            return self.head.value

    def __repr__(self):
        if self.head == None:
            return 'NULL'
        else :
            values=''
            temporary_value=self.head
            while temporary_value:
                values+=f'{temporary_value.value}'  + '-> '
                temporary_value=temporary_value.next
            values=values +'NULL'
            return f'{values}'


    def Inbetween(self,middle_node,newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return

      NewNode = Node(newdata)
      NewNode.value = middle_node.value
      middle_node.value = NewNode


    def append(self,value):
        current=self.head
        if self.head ==None:
            self.head=Node(value)
            return self.head.value
        else:
            while current.next:
                current=current.next
            current.next=Node(value)
            return current.next

    


l=LinkedList()
l.append(50)
l.append(40)
l.append(30)
l.append(20)
l.append(10)

l.Inbetween(2, 300)
print(l)