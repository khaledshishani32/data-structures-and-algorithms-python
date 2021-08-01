from linked_list_insertions import __version__

from linked_list_insertions.linked_list_insertion import (LinkedList,Node)

def test_version():
    assert __version__ == '0.1.0'





def test_multiple():
    
    l=LinkedList()
    l.append(2)
    l.append(8)
    actual=l.__str__()
    expected='2-> 8-> NULL'
    assert actual==expected