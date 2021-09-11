class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    
    def display(self):
        output = []
        # traverse linked list and add to output
        current = self.head
        while current:
            output.append(current.value)
            current = current.next
        return output

class HashTable:

  def __init__(self,size=521) -> None:
      self.bucket=[None]* size
      self.size= size

  def add(self,key,value):
    index = self.hash(key)

    if self.bucket[index] is None:
      self.bucket[index]=LinkedList()
    self.bucket[index].add([key,value])




  def get(self,key):
    index = self.hash(key)
    if self.bucket[index] is None:
      return None
    else:
      current = self.bucket[index].head
      while current:
        if current.value[0] == key:
            return current.value[1]
        current = current.next



  def contains(self,key):
    index = self.hash(key)
    if self.bucket[index] == None:
      return False
    else:
      current = self.bucket[index].head
      while current:
        if current.value[0] == key:
            return True
        else:
          return False



  def hash(self,key):
    value= 0
    for character in key:
      value+= ord(character)
    idx = value * 7 % self.size
    return idx
  

  
def repeated_word(input_string):

    if not input_string:
        return "The input_string is empty"

    input_string = input_string.replace(".", "")
    input_string = input_string.replace(",", "")
    input_string = input_string.lower()

    words = input_string.split()

    hash_obj = HashTable()

    for word in words:

        if hash_obj.contains(word):
            return word

        else:
            hash_obj.add(word, word)

    return "No repeated word ! "

    



if __name__ == "__main__":
  
  print(repeated_word('Once upon a time, there was a brave princess who...'))