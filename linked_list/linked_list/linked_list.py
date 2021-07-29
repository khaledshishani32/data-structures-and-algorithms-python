


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value='null'):
        
        try:
          new_node = Node(value)
          if not self.head:
              self.head = new_node
          else:
              current_value = self.head
              self.head= new_node
              self.head.next=current_value
        except Exception as e:
          raise Exception(f"Something's Going Wrong : {e}")
    def includes(self,num):
       
        try:
          x=False
          current_value = self.head
          while current_value:
              if current_value.value==num:
                  x=True
                  break
              current_value=current_value.next
          return x
        except Exception as e:
          raise Exception(f"Something's Going Wrong : {e}")
    def __str__(self):
        
        output = ''
        current_value = self.head
        while current_value:
            value = current_value.value
            if current_value.next is None:
                output += f"( {value} ) -> null"
                break
            output = output + f"( {value} ) -> "
            current_value=current_value.next
        return output




if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert(12)
    l1.insert(22)
    l1.insert(30)
    l1.insert(50)
    l1.insert(70)
    print(l1.__str__())    