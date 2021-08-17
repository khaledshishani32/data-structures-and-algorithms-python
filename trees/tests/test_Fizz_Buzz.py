from trees.tree import *



def test_fizz_buzz():
    tree = Binary_s_tree(8)
    tree.insert(10)

    tree.insert(3)
    tree.insert(1)
    tree.insert(6)
    tree.insert(4)
    tree.insert(7)
    tree.insert(14)
    tree.insert(13)
    tree.insert(15)

    assert tree.fizz_buzz() ==[1, 'Fizz', 4, 'Fizz', 7, 8, 'Buzz', 13, 14, 'FizzBuzz']