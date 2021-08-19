

class Binary_s_tree:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = 1 
        
    def insert(self,data):
        if self.data == data:
            return False #     duplicate data
        elif self.data > data:
            if self.left is not None:
                self.size+=1
                
                return self.left.insert(data)
                
            else:
                self.left=Binary_s_tree(data)
                self.size+=1
                return True
        else:
            if self.right is not None:
                self.size+=1
                return self.right.insert(data)
            else:
                 self.right = Binary_s_tree(data)
                 self.size+=1
                 return True      

    def find(self, data):
        if self.data == data:
            return True
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data) # 
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)

    def preorder(self):
        if self is not None:
            print(self.data ,end="-->")
            if self.left is not None:
                self.left.preorder()
            
            if self.right is not None:
                self.right.preorder()
    
        
     
    def inorder(self):
        elements=[]
        if self.left:
            elements+=self.left.inorder()
        elements.append(self.data)

        if self.right:
            elements+=self.right.inorder()
        return elements
    
    def sum_odd_values(self):
        my_list=self.inorder()
        sum_of_values=0
        result = list(filter(lambda x: (x % 2 != 0), my_list))
        print(result)
        for i in result:
            sum_of_values+=i
        return sum_of_values    


    def fizz_buzz(self):
        my_list = self.inorder()
        restult = []
        for i in my_list:
            if i % 3 == 0 and i % 5 == 0:
                restult.append("FizzBuzz")
            elif i % 3 == 0 :
                restult.append("Fizz")
            elif i % 5 == 0 :
                restult.append("Buzz")
            else:
                restult.append(i)            
        return restult 
    
    def max_tree_value(self):
       my_list =self.inorder()
       return my_list[len(my_list)-1]


    def postorder(self):
        if self is not None:
            if self.left is not None:
                self.left.postorder()
            
            if self.right is not None:
                self.right.postorder() 
            print(self.data , end=" ")
            return
    
    def is_empty(self):
        return self.size == 0
    
    def __str__(self):
        return self.data

    def max_tree_value(self):
       my_list =self.inorder()
       return my_list[len(my_list)-1]
        


if __name__ == '__main__':

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
    print(tree.sum_odd_values())
    # print(tree.inorder())
    # print(tree.fizz_buzz())
# # print(tree.right.left.data)
# # # print(tree.right.right.data)

# print(tree.find(10))            
# print(tree.preorder())
# tree.inorder()
# print()
    
    # print(tree.max_tree_value())
# print(type(inorder_list[0]))
# print(tree.list)
# t=tree.postorder()
# print()

# print(type(t))
# print(tree.is)
# print(tree.__str__())