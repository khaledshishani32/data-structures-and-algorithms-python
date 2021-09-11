
from hashtable.LinkedList import *



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
  
  # print(hash.find_value('Once upon a time, there was a brave princess who...'))

  # print(hash.contains('22'))
  # print(hash.contains('30'))