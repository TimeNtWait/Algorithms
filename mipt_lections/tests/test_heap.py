import pytest
from mipt_lections.heap.heap import Heap


@pytest.fixture(scope="module")
def create_heap():
    heap = Heap()
    yield heap


def test_heap(create_heap):
    # Создаем Кчу
    heap = create_heap
    # Добавляем элементы в кучу
    heap.push(7)
    print(heap)
    assert heap.levels() == 1
    heap.push(15)
    heap.push(6)
    top_item_heap = heap.pop()
    assert top_item_heap == 15
    heap.push(-1)
    heap.push(12)
    print(heap)

