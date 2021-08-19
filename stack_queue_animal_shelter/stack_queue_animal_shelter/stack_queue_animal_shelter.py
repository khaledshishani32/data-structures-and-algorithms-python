
class Node:
  def __init__(self,value):
    self.value= value
    self.next= None
  
class Queue():
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def enqueue(self,value):
        node=Node(value)
        if self.front==None:
            self.front=node
            self.rear=node
            self.size+=1
            return self.rear.value
        else:
            self.rear.next=node
            self.rear=node
            self.size+=1
            return self.rear.value

    def dequeue(self):
        try:
            if self.front == None:
              raise Exception
            temp=self.front
            self.front=self.front.next
            self.size-=1
            return temp.value
        except Exception:
            return 'The queue is empty you cannot dequeue'

    def is_empty(self):
        return self.size==0

    def peek (self):
        try:
            if self.front == None:
                raise Exception
            return self.front.value

        except Exception:
            return 'Empty Queue'



class AnimalShelter:
    def __init__(self):
        self.cat=Queue()
        self.dog=Queue()
        self.count=0

    def enqueue(self,animal,animal_type):
        animal_type=animal_type.lower()
        if animal_type =='cat':
            self.count+=1
            return self.cat.enqueue(animal)

        elif animal_type=='dog':
            self.count+=1
            return self.dog.enqueue(animal)

        else:
            return None


    def dequeue(self,animal_type):
        animal_type=animal_type.lower()
        if self.is_empty()==False:
         if animal_type == 'dog':
            return self.dog.dequeue()
         if animal_type =='cat':
               return self.cat.dequeue()
         else:
            return None
        else:
            print('The queue is empty you cannot dequeue')

    def is_empty(self):
        return self.count == 0


if __name__=="__main__":
    q=AnimalShelter()
    print(q.enqueue('lily','dog'))
    print(q.dequeue('dog'))
    # # print(q.enqueue("locy", "hoo"))
    # print(q.is_empty())

    q1=Queue()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.dequeue()
    q1.dequeue()
    print(q1.dequeue())

    print(q1.is_empty())