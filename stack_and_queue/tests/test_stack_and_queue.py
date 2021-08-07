from stack_and_queue import __version__

import pytest

from stack_and_queue.stack_and_queue import Stack, Queue, QueueEmptyException , StackEmptyException

# def test_version():
#     assert __version__ == '0.1.0'


# stack testing
#1
def test_push_one_value_to_stack():

    s = Stack()
    s.push(10)

    assert s.is_empty() == False

#2
def test_push_multiple_value_to_stack():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    assert s.is_empty() ==False
#3
def test_pop_stack():

    s = Stack()
    s.push(10)
    s.pop()

    assert s.is_empty() == True
#4
def test_is_empty_after_multiple_pop_stack():

    s = Stack()
    s.push(10)
    

    with pytest.raises(StackEmptyException, match ="This stack is empty, therefore cannot pop any elelment !." ):
     s.pop()
     s.pop()

#5
def test_peek_stack():

    s = Stack()
    s.push(10)
    s.push(20)
    

    assert s.peek() == 20


#6
def test_empty_after_instantiate_stack():

    s = Stack()
   

    assert s.is_empty() == True

#7
def test_call_peek_or_pop_with_empty_stack():

    s=Stack()

    with pytest.raises(StackEmptyException, match ="This stack is empty, therefore cannot peek any element !." ):
     s.peek()




# queue testing 

#1
def test_enqueue_to_queue():

    q = Queue()
    q.enqueue(10)

    assert q.is_empty() == False


#2
def test_enqueue_multiple_value_to_queue():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)

    assert q.is_empty() == False

#3
def test_dequeue_queue():

    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()

    assert q.is_empty() == False 

#4
def test_peek_queue():

    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    

    assert q.peek() == 10

#5
def test_empty_after_multi_dequeue():

    q=Queue()
    q.enqueue(10)

    with pytest.raises(QueueEmptyException, match ="This queue is empty, therefore cannot dequeue any elelment !." ):
     q.dequeue()
     q.dequeue()

#6
def test_empty_after_instantiate_queue():

    q=Queue()
    

    with pytest.raises(QueueEmptyException, match ="This queue is empty, therefore cannot dequeue any elelment !." ):
     q.dequeue()

#7
def test_peek_or_pop_if_queue_empty():

    q=Queue()
    

    with pytest.raises(QueueEmptyException, match ="This queue is empty, therefore cannot peek any element !." ):
     q.peek()