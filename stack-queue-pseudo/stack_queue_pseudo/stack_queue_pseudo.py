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
 
class PseudoQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.secand_stack = Stack()
        self.rear = None
        self.front = None
       

    def enqueue(self, data):
        self.first_stack.push(data)
        self.rear = self.first_stack.top.data
       

    def dequeue(self):
        if self.first_stack.top:
            stack1 = self.first_stack
            while not stack1.is_empty():
                self.secand_stack.push(stack1.pop())
               

            poped = self.secand_stack.pop()
            self.front = self.secand_stack.top
            self.first_stack = Stack()
            stack2 = self.secand_stack
            while not stack2.is_empty():
                self.first_stack.push(stack2.pop())
                
            return poped

    def peek_rear(self):
        return self.rear

if __name__== "__main__" :
    queue= PseudoQueue()
    queue.enqueue(10)
    queue.enqueue(15)
    
    print(queue.peek_rear())
   
   
    
