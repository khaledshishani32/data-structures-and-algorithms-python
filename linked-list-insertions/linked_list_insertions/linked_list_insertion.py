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
 
 

def zipLists(head1, head2):
 
    temp = None
 
    if head1 is None:
        return head2
 
    if head2 is None:
        return head1
 
    if head1.data <= head2.data:
        temp = head1
        temp.next = zipLists(head1.next, head2)
         
    else:
        temp = head2
        temp.next = zipLists(head1, head2.next)

    return temp
 
 

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