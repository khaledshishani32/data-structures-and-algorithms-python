from stack_queue_animal_shelter import __version__

from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter

def test_version():
    assert __version__ == '0.1.0'


def test_expected_outcome():
    q=AnimalShelter()
    actual=q.enqueue('jack','dog')
    expected='jack'
    assert expected==actual


def test_edge_cases():
    q=AnimalShelter()
    actual=q.is_empty()
    assert actual== True


def test_expected_failure():
    q=AnimalShelter()
    actual=q.enqueue('katty','snake')
    expected= None
    assert expected==actual