import random
from array_structure import FixedArray
from list_structure import LinkedList
from deque_structure import Deque
from avl_tree import AVLTree
from bubble_sort import bubble_sort
from quick_sort import quick_sort


def main():
    print("--- 1. ПРОВЕРКА МАССИВА ---")
    arr = FixedArray(3)
    arr.set(0, "First")
    arr.set(1, "Second")
    print("Index 0:", arr.get(0))
    print("Index 1:", arr.get(1))

    print("\n--- 2. ПРОВЕРКА СПИСКА ---")
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    print("Head:", ll.head.value)
    print("Next:", ll.head.next.value)

    print("\n--- 3. ПРОВЕРКА ДЕКА ---")
    d = Deque()
    d.append_left("Left")
    d.append_right("Right")
    print("Pop Left:", d.pop_left())
    print("Pop Right:", d.pop_right())

    print("\n--- 4. ПРОВЕРКА АВЛ-ДЕРЕВА ---")
    tree = AVLTree()
    for num in [10, 20, 30, 5, 15]:   # <-- здесь был пропущен список
        tree.insert(num)
    print("Inorder:", tree.inorder())

    print("\n--- 5. ПРОВЕРКА СОРТИРОВОК ---")
    test_data = [random.randint(1, 100) for _ in range(5)]
    print("Original:", test_data)
    print("Bubble:", bubble_sort(test_data.copy()))
    print("Quick:", quick_sort(test_data.copy()))


if __name__ == "__main__":
    main()