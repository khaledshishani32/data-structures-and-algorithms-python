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
  

  # i tarying to find the first duplicate by using add method but i cannot know how to solev the problem 
  # i think need to using also the contanis 

  def find_value(self, value_stirng):
    value_stirng =value_stirng.split('')
    for i in value_stirng:
      j = 1 
      self.add(j , i )
      j+=1

    



if __name__ == "__main__":
  hash=HashTable()

  hash.add('1','khaled')
  hash.add('2', 'waleed')
  for i in range(1,3):
    i =  str(i)
    print(hash.get(i))
  # print(hash.get(1))
  # hash.add('3', 'Once upon a time, there was a brave princess who...')