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

    def __str__(self):
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

    def printNthFromLast(self, n):
        temp = self.head 
        n+=1
        length = 0
        while temp:
            temp = temp.next
            length += 1

        if n > length: 
            raise Exception("Location is greater than the length of LinkedList")
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        return temp.value


l = LinkedList()
l.append(1)
l.append(3)
l.append(8)
l.append(2)
l.printNthFromLast(0)
### 3 cases work 0 , 2 , grater the length (6)

print(l.printNthFromLast(0))
print(l.printNthFromLast(2))
print(l.printNthFromLast(6))