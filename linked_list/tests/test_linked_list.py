from linked_list import __version__

from linked_list.linked_list import (LinkedList,Node)

def test_version():
    assert __version__ == '0.1.0'





def test_empty_linked_list():

    test=LinkedList()
    test.insert()
    actual=test.__str__()
    expected='(null) -> null'
    assert actual==expected


def test_insert():

    test=LinkedList()
    test.insert(55)
    actual=test.head.value
    expected=55
    assert actual==expected


def test_first():

    test=LinkedList()
    test.insert(55)
    test.insert(77)
    test.insert(88)
    test.insert(99)
    actual=test.head.value
    expected=99
    assert actual==expected


def test_multiple():

    test=LinkedList()
    test.insert(2)
    test.insert(8)
    actual=test.__str__()
    expected='(8) -> (2) -> null'
    assert actual==expected

def test_return_true():

    test=LinkedList()
    test.insert('khaled')
    test.insert('shosh')
    actual=test.includes('khaled')
    expected=True
    assert actual==expected

def test_return_false():

    test=LinkedList()
    test.insert('khaled')
    test.insert('shishani')
    actual=test.includes('shosh')
    expected=False
    assert actual==expected


def test_all_collection():

    test=LinkedList()
    test.insert("shishani")
    test.insert("abu baker")
    test.insert("waleed")
    test.insert("khaled")
    actual=test.__str__()
    expected='(khaled) -> (waleed) -> (abu baker) -> (shishani) -> null'
    assert actual==expected

