class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top == None:
            self.top = node 
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if not self.is_empty():
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.data
        else:
            return "This is Empty stack"

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            raise Exception("The satck empty cannot peek !")
        return self.top.data
 
class PseudoQueue :
    def __init__(self):
        self.first_s=Stack()
        self.second_s=Stack()
        self.rear=None
        self.front=None
        self.size=0

    def enqueue(self , data):
        self.first_s.push(data)
        self.rear=self.first_s.top.data
        self.size+=1
   

    def dequeue(self):
        if self.first_s.top :
            temp = self.first_s
            while not temp.is_empty():
                self.secand_stack.push(temp.pop())
                self.size-=1

            poped = self.secand_stack.pop()
            self.front = self.secand_stack.top
            self.first_s = Stack()
            temp2 = self.secand_stack
            while not temp2.is_empty():
                self.first_s.push(temp2.pop())
                self.size-=1
            return poped

    def is_empty(self):
        return self.size == 0

    def desplay(self):
        queue_str=''
        temp = self.first_s.top
        while temp:
            queue_str+= '(' +str(temp.data)+ ')'+ '-->'
            temp=temp.next
        print(queue_str + "None")
    
    def peek(self):
        return self.rear

if __name__== "__main__" :
    queue= PseudoQueue()
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)

    queue.enqueue(50)
    print(queue.peek())
    queue.desplay()
