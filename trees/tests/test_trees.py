from trees import __version__

from trees.tree import *  

def test_version():
    assert __version__ == '0.1.0'


def test_instantiate_empty_tree():
   tree = Binary_s_tree()

   assert tree.data==None


def test_single_root():
 tree = Binary_s_tree(10)

 assert tree.data==10

def test_left_right_single_root():
 tree = Binary_s_tree(10)
 tree.insert(7)
 tree.insert(15)

 assert tree.data==10
 assert tree.right.data==15
 assert tree.left.data==7


# def test_preorder():
#  tree = Binary_s_tree(10)
#  tree.insert(15)
#  tree.insert(20)
#  tree.insert(13)
#  tree.insert(7)
#  tree.insert(4)
#  tree.insert(9)
 
#  assert  tree.preorder() =='10-->7-->4-->9-->15-->13-->20-->'


def test_inorder():
 tree = Binary_s_tree(10)
 tree.insert(15)
 tree.insert(20)
 tree.insert(13)
 tree.insert(7)
 tree.insert(4)
 tree.insert(9)
 
 assert  tree.inorder() =='10-->7-->4-->9-->15-->13-->20-->'
