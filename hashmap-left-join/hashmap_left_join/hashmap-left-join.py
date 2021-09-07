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
  
        current = self.head
        while current:
            output.append(current.value)
            current = current.next
        return output


class HashTable:

    def __init__(self, size=521) -> None:
        self.bucket = [None] * size
        self.size = size

    def add(self, key, value):
        index = self.hash(key)

        if self.bucket[index] is None:
            self.bucket[index] = LinkedList()
        self.bucket[index].add([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.bucket[index] is None:
            return None
        else:
            current = self.bucket[index].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next

    def contains(self, key):
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

    def hash(self, key):
        value = 0
        for character in key:
            value += ord(character)
        idx = value * 7 % self.size
        return idx


def hashmap_left_join(hash_one,hash_two):
    result=[]
    if hash_one.bucket is  hash_one.size*[None] or hash_two.bucket is hash_two.size*[None] :
        return None
    for val in hash_one.bucket:
        if val:
            temp=[]
            temp.append(val.head.value[0])
            temp.append(hash_one.get(val.head.value[0]))
            temp.append(hash_two.get(val.head.value[0]))
            result.append(temp)
    return result

if __name__ == "__main__":
    hash_one = HashTable()

    hash_one.add('fond', 'enamored')
    hash_one.add('wrath', 'anger')
    hash_one.add('diligent', 'employed')
    hash_one.add('outfit', 'grap')
    hash_one.add('guide', 'usher')

    hash_two = HashTable()

    hash_two.add('fond', 'averse')
    hash_two.add('wrath', 'delight')
    hash_two.add('diligent', 'idle')
    hash_two.add('guide', 'follow')
    hash_two.add('flow', 'jam')

    print(hashmap_left_join(hash_one,hash_two))
