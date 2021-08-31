from quick_sort.quick_sort import quick_sort
from quick_sort import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_quick_sort():
    my_list=[8,4,23,42,16,15]
    assert  quick_sort(my_list , 0 , 5 ) == [4, 8, 15, 16, 23, 42]
