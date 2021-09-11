
from hashmap_repeated_word import __version__

from hashmap_repeated_word.hashmap_repeated_word import *
def test_version():
    assert __version__ == '0.1.0'



def test_reapeted_word():

    actual = repeated_word('Once upon a time, there was a brave princess who...')
    excepted = "a"
    assert actual == excepted

