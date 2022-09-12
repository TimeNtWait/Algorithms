import pytest
from Sorting.Sorting import Sort


@pytest.fixture(scope="module")
def create_sort():
    s = Sort()
    yield s


@pytest.mark.parametrize(
    ("input_seq", "sorted_seq"), [
        ([5, 6, 2, 1, 3, 4], [1, 2, 3, 4, 5, 6]),
        ([0, 1, -1], [-1, 0, 1]),
        ([3, 2, 5, 6, 3, 7, -7, -7], [-7, -7, 2, 3, 3, 5, 6, 7]),
        ([4, 9, 0, 3], [0, 3, 4, 9]),
        ([1, 1, 2, 0], [0, 1, 1, 2]),
    ]
)
def test_insert_sort(create_sort, input_seq, sorted_seq):
    """Тестируем все алгоритмы сортировки на одном наборе данных"""
    s = create_sort

    # Важно, что в качестве параметра переадем не просто input_seq
    # (как ссылку на объект input_seq), а как копию объекта input_seq,
    # через конструкцию input_seq[:]. Это важно чтобы убедиться, что
    # каждая тестируемая функция будет работать с изначальной
    # неотсортированной последовательностью.
    # Сортировка вставкой
    assert s.insert_sort(input_seq[:]) == sorted_seq
    # Сортировка выбором
    assert s.choice_sort(input_seq[:]) == sorted_seq
    # Сортировка пузырьком
    assert s.bubble_sort(input_seq[:]) == sorted_seq
    # Сортировка подсчетом частот
    # Работает только для положительных чисел, также необходмио заранее
    # знать максимальный диапозон чисел
    if min(input_seq) > 0:
        assert s.calc_freq_sort(input_seq[:], sort_range = (max(input_seq)+1) ) == sorted_seq
    # Быстрая сортировкаа по методу Тони Хоара
    assert s.fast_sort(input_seq[:]) == sorted_seq
    # Сортировка слиянием (слияние отсортированных массивов)
    assert s.half_sort(input_seq[:]) == sorted_seq
