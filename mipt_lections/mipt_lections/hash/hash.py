"""Hash таблица
Реализация через открытую адресацию, что означает что при коллизии элементы
с одинсковым хэш адресом хранятся в hash-таблице в виде односвязанного списка.

methods:
- add(value: int) - Добавление элемента в hash-таблицу
- exist(value: int) -> bool -  Проверка нахождения элемента в hash-таблице
- calc_hash(value: int) -> int - Рассчет хеша от входных данных.
# doctest
>>> h = HashTable()
>>> print(h.calc_hash(2123))
114
>>> print(h.calc_hash(0))
64
>>> print(h.calc_hash(-12343))
93
>>> h.add(7)
>>> h.add(3)
>>> h.add(2)
>>> print(h.exist(5))
False
>>> print(h.exist(7))
True
"""
from linkedlist import LinkedList

# Размер hash таблицы. Должен быть соизмеримо больше. Рекомендуемый размер: в
# 1.3 раза больше максимального кол-ва ключей хранимых в таблице
HASH_SIZE = 256


class HashTable():
    def __init__(self):
        # Каждый элемент hash-таблицы представляет из себя односвязанный список
        self.table = [LinkedList() for _ in range(HASH_SIZE)]

    def add(self, value: int):
        """Добавление элемента в hash-таблицу с предварительным расчетом хэша"""
        h = self.calc_hash(value)
        self.table[h].push(value)

    def exist(self, value: int) -> bool:
        """Проверка нахождения элемента в hash-таблице по след.алгоритму:
         - рассчет хэша от искомого элемента
         - получение по хэшу односвязанного списка из hash-таблицы
         - проверка в наличия элемнта в односвязанном списке
         """
        h = self.calc_hash(value)
        return self.table[h].include(value)

    def calc_hash(self, value: int) -> int:
        """Рассчет хеша от входных данных.
        Требования:
        - Соблюдение однозначности, т.е. для одних тех же входных данных должен
        быть рассчитан одинаковый хэш
        - Итоговый хэш должен лежать в рамках допустимого значения HASH_SIZE
        для этого от итогового хэша берется отсаток от HASH_SIZE
        """
        value = abs(value) * 54321
        h_key = 123456
        while value > 0:
            h_key = h_key + 3 * value % 10
            value = value // 10
        return int(h_key) % HASH_SIZE

    def __str__(self) -> str:
        return f"{self.table}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
