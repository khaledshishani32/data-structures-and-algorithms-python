from stack_queue_animal_shelter import __version__

from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter

def test_version():
    assert __version__ == '0.1.0'


def test_expected_outcome():
    q=AnimalShelter()
    actual=q.enqueue('lily','dog')
    expected='lily'
    assert expected==actual


def test_edge_cases():
    q=AnimalShelter()
    actual=q.is_empty()
    assert actual== True


def test_expected_failure():
    q=AnimalShelter()
    actual=q.enqueue('momo','camel')
    expected= None
    assert expected==actual

def test_expected_outcome_dequeue():
    q=AnimalShelter()
    actual=q.enqueue('momo','cat')
    actual=q.dequeue('cat')
    expected='momo'
    assert expected==actual

def test_edge_case_dequeue():
    q=AnimalShelter()
    actual=q.dequeue('cat')
    expected=None
    assert actual==expected

def test_expected_failure_dequeue():
    q=AnimalShelter()
    actual=q.enqueue('momo','cat')
    actual=q.enqueue('momo','dog')
    actual=q.dequeue('fish')
    expected=None
    assert expected==actual