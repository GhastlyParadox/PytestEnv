import pytest
from linked_lists.linked import CLinkedList
from value_gen.values import ValueGenerator


def test_tail_insert():
    # single insertion test at tail
    linked = CLinkedList()
    linked.insertAtTail(8)
    linked.insertAtTail(7)
    assert linked.__len__() == 2
    assert linked.tail.value == 7


def test_tail_insert_values():
    # multivalue insertion test at tail
    linked = CLinkedList()
    gen = ValueGenerator()
    vals = gen.fibArr(8)
    linked.insertAtTail(vals)
    assert linked.tail.value == 13


def test_head_insert():
    # single insertion test at head
    linked = CLinkedList()
    linked.insertAtHead(8)
    assert linked.__len__() == 1
    assert linked.tail.value == 8


def test_head_insert_values():
    # multivalue insertion test at head
    linked = CLinkedList()
    gen = ValueGenerator()
    vals = gen.fibArr(8)
    linked.insertAtHead(vals)
    assert linked.__len__() == 8


def test_get_node_by_index():
    linked = CLinkedList()
    linked.insertAtHead([4, 1, 3, 7, 5])
    assert linked.getNodeByIndex(1).value == 7

