#create NODE class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class StackEmptyException(Exception):
	pass


class QueueEmptyException(Exception):
	pass

#create stack class
class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        node = Node(data)
        if self.top:
          node.next = self.top
          self.top = node
        else :
            self.top=node 
     
    def is_empty(self):
        return not self.top 

    def pop(self):
        if self.is_empty():
            raise StackEmptyException('This stack is empty, therefore cannot pop any elelment !.')

        result= self.top.data
        self.top=self.top.next
        return result
        

    def peek(self):
        if self.is_empty():
            raise StackEmptyException('This stack is empty, therefore cannot peek any element !.')

        return self.top.data      


#create queue class

class Queue():
    def __init__(self):
        self.front=None
        self.rear=None
    

    def enqueue(self , data):
        node=Node(data)
        if self.front ==None:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node    
            self.rear=node
     

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyException('This queue is empty, therefore cannot dequeue any elelment !.')
        
        temp=self.front
        self.front=temp.next
        temp.next=None
        return temp.data

    def peek(self):
        if self.is_empty():
            raise QueueEmptyException('This queue is empty, therefore cannot peek any element !.')

        return self.front.data 
        
    def is_empty(self): 
        return not self.front or not self.rear




# if __name__ == "__main__":
   


