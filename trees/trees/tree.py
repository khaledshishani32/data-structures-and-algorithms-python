class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class Binary_tree:
    def __init__(self):
        self.root = None

    def pre_order(self):

        values = ''
        if not self.root:
            return 'The Tree is empty'

        def traverse(node):
            nonlocal values 
            values += str(node.value) 

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)
                  
        traverse(self.root)

        return values
    
    def post_order(self):
        values = ''
        if not self.root:
            return 'The Tree is empty'
        
        def traverse(node):
            nonlocal values 

            if node.left:
                
                traverse(node.left)
                
            if node.right:
                traverse(node.right)

            values += str(node.value)       

        
        traverse(self.root)
         
        return values

    def in_order(self):
        values = ''
        if not self.root:
            return 'The Tree is empty'
        
        def traverse(node):
            nonlocal values 

            if node.left:
                
                traverse(node.left)

            values += str(node.value)
                
            if node.right:
                traverse(node.right)

        traverse(self.root)
         
        return values

