import pytest
from linked_lists.linked import SLList
from value_gen.values import ValueGenerator


def test_insertAtHead():
    linked = SLList()
    gen = ValueGenerator()
    vals = gen.fibArr(15)
    linked.insertAtHead(vals)
    assert linked.__len__() == 15
    linked.insertAtHead(16)
    assert linked.__len__() == 16