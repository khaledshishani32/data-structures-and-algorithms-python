
class QueueEmptyException(Exception):
	pass

class Node:
  def __init__(self,value):
    self.value= value
    self.next= None

class Queue():
    def __init__(self):
        self.front=None
        self.rear=None


    def enqueue(self,value):
        node=Node(value)
        if self.front==None:
            self.front=node
            self.rear=node
            return self.rear.value
        else:
            self.rear.next=node
            self.rear=node
            return self.rear.value

    def dequeue(self):
        if self.is_empty():
             raise QueueEmptyException('This queue is empty, therefore cannot dequeue any elelment !.')

             temp=self.front
             self.front=self.front.next
             return temp.value
        

    def is_empty(self): 
        return not self.front or not self.rear

    def peek(self):
        if self.is_empty():
             raise QueueEmptyException('This queue is empty, therefore cannot peek any element !.')

        return self.front.data 

      



class AnimalShelter:
    def __init__(self):
        self.cat=Queue()
        self.dog=Queue()
        self.total=0

    def enqueue(self,animal,animal_type):
        if animal_type =='cat':
            self.total+=1
            return self.cat.enqueue(animal)
        elif animal_type=='dog':
            self.total+=1
            return self.dog.enqueue(animal)
        else:
            return "Please Enter either dog or cat !" 
            

    def dequeue (self,animal_type):
        if self.is_empty():
             raise QueueEmptyException('This queue is empty, therefore cannot dequeue any elelment !.')
        if animal_type == 'dog':
            return self.dog.dequeue()
        if animal_type =='cat':
            return self.cat.dequeue()
        else:
            return None
        


    def is_empty(self):
        if self.total > 0:
            return False
        else:
            return True


if __name__=="__main__":
    q=AnimalShelter()
    # print(q.enqueue('mishmish','dog'))
    # print(q.enqueue('rose','cat'))
    print(q.dequeue("dog"))
    print(q.is_empty())