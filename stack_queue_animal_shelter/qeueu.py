
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


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
    

    # def __repr__(self):

    #     itr = self.head
    #     while self.next:
     

    def display(self):
        if self.front is None:
            print("The queue list is empty !!")
            return
               

        itr = self.front
        llstr=''

        while itr:
            llstr +=str(itr.data) + ' --> '
            itr=itr.next    
        print(llstr + 'None')    

    def duckDuckGoose(self,k):
         my_list=["A" , ]
         itr = self.front
         while itr:
            
            itr=itr.next    
         print(itr) 


    

if __name__=="__main__":

    q=Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")
    q.enqueue("E")
    print(q.)
   