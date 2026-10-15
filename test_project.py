import pytest
from array_structure import FixedArray
from list_structure import LinkedList
from deque_structure import Deque
from avl_tree import AVLTree, AVLNode
from bubble_sort import bubble_sort
from quick_sort import quick_sort

def test_array():
    arr = FixedArray(5)
    arr.set(0, 10)
    assert arr.get(0) == 10
    with pytest.raises(IndexError):
        arr.get(10)

def test_linked_list():
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    assert ll.head.value == 5
    assert ll.head.next.value == 10

def test_deque():
    d = Deque()
    d.append_right(1)
    d.append_left(2)
    assert d.pop_left() == 2
    assert d.pop_right() == 1
    assert d.pop_left() is None

def test_avl_tree():
    tree = AVLTree()
    tree.root = AVLNode(15)
    assert tree.root.key == 15
    assert tree.root.height == 1

def test_bubble_sort():
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert bubble_sort(data) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_quick_sort():
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert quick_sort(data) == [1, 1, 2, 3, 4, 5, 5, 6, 9]