
from trees.tree import Binary_s_tree



def max_tree_value(self):
       my_list =self.inorder()
       return my_list[len(my_list)-1]



if __name__ == '__main__':

    tree = Binary_s_tree(10)
    tree.insert(15)

    tree.insert(20)
    tree.insert(13)
    tree.insert(7)
    tree.insert(4)
    tree.insert(9)
    tree.insert(80)
    tree.insert(200)