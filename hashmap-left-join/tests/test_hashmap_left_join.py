from hashmap_left_join import __version__

from hashmap_left_join.hashmap_left_join import *
def test_version():
    assert __version__ == '0.1.0'



def test_join_left():
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
    
    actual = hashmap_left_join(hash_one,hash_two)
    excepted = [['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse'], ['outfit', 'grap', 'NULL']]
    assert actual == excepted