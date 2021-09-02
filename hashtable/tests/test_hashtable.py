from hashtable import __version__

from hashtable.hashtable import * 

# def test_version():
#     assert __version__ == '0.1.0'


def test_add_hash():

  hash=HashTable()

  hash.add('1','khaled')
  hash.add('2', 'waleed')
  hash.add('3', 'al shishani')

  assert hash.contains("1")==True

def test_Retrieving_based_on_a_key_returns_the_value_stored():
    hash=HashTable()

    hash.add('1','khaled')
    hash.add('2', 'waleed')
    hash.add('3', 'al shishani')

    assert hash.get("1") == "khaled"

def test_Successfully_returns_null_for_akey_that_does_not_exist_in_the_hashtable():
    hash=HashTable()

    hash.add('1','khaled')
    hash.add('2', 'waleed')
    hash.add('3', 'al shishani')

    assert hash.get("50") == None


