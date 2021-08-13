class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 

class LinkedList:
 
  
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
         
        while temp :
            print(temp.data, end="->")
            temp = temp.next
 

    def append(self, new_data):
        new_node = Node(new_data)
         
        if self.head is None:
            self.head = new_node
            return
        last = self.head
         
        while last.next:
            last = last.next
        last.next = new_node
 
 


 
 

if __name__ == '__main__':
 
   
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)

 
  
    list2 = LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)
 
    list3 = LinkedList()
 
    list3.head = zipLists(list1.head, list2.head)
 
    list3.printList()