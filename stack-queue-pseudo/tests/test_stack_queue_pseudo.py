from stack_queue_pseudo import __version__

from stack_queue_pseudo.stack_queue_pseudo import *

def test_version():
    assert __version__ == '0.1.0'


def test_size_after_enqueue():
    queue = PseudoQueue()
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    queue.enqueue(50)

    acual = queue.is_empty()
    expected = False
    assert acual == expected


def test_is_last_in_first_out():

    queue = PseudoQueue()
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    queue.enqueue(50)

    acual = queue.peek()
    expected = 50
    assert acual == expected


def test_after_dequeue():

    queue = PseudoQueue()
    queue.enqueue(10)
    queue.enqueue(15)

    acual = queue.peek_rear()
    expected = 15
    assert acual == expected    