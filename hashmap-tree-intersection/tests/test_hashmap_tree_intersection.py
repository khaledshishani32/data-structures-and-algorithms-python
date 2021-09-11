from hashmap_tree_intersection import __version__

from hashmap_tree_intersection.hashmap_tree_intersection import *

def test_version():
    assert __version__ == '0.1.0'




def test_hashmap_tree_intersection():
    tree1 = B_tree()
    tree1.insert(10)
    tree1.insert(20)
    tree1.insert(30)
    tree1.insert(40)
    tree1.insert(50)
    tree1.insert(600)
    
    
    tree2 = B_tree()
    tree2.insert(10)
    tree2.insert(20)
    tree2.insert(30)
    tree2.insert(40)
    tree2.insert(50)
    tree2.insert(7)
   
    actual = intersection(tree1 , tree2)
    excepted = [10, 20, 30, 40, 50]

    assert actual == excepted
