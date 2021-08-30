from mergesort import __version__

from mergesort.merge_sort import *


def test_version():
    assert __version__ == '0.1.0'



def test_merge_sort():
    my_list = [30,27,43,3,9,62,10]
    acual =merge_sort(my_list , 0 , 6)
    excepted = [3, 9, 10, 27, 30, 43, 62]
    assert acual == excepted

