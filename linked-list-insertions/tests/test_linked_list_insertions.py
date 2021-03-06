from linked_list_insertions import __version__

from linked_list_insertions.linked_list_insertion import LinkedList,Node , zipLists

def test_version():
    assert __version__ == '0.1.0'

#test code challenge class 07

def test_cal_NthFromLast():
    l = LinkedList()
    l.append(1)
    l.append(3)
    l.append(8)
    l.append(2)
    actual=l.printNthFromLast(2)
    expected=3
    assert actual==expected

def test_merge():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2 = LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)

    list3 = LinkedList()


    actual=list3.head = zipLists(list1.head, list2.head)
    expected="1->3->2->5->9->4->"
    assert actual==expected


# def test_if_N_Greater_than_length():
#     l = LinkedList()
#     l.append(1)
#     l.append(3) 
#     l.append(8)
#     l.append(2)
#     actual=l.printNthFromLast(6)
#     expected=3
#     assert actual=="Location is greater than the length of LinkedList"
