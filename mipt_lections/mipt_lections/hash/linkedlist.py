"""Односвязный список
Структура даных, которая представляет собой иерархически вложенный список вида:
[1,[2,[3,[8,[7,[None]]]]]]
где первым элементом ялявется значение элемента,
а вторым ссылка на следующий элемент
Данная структура позволяет быстро (O(1)) добавлять и удалять элементы,
недостатком является долгий (O(N)) доступ к элементу по индексу

>>> a = LinkedList()
>>> a.push(3)
>>> a.push(2)
>>> a.push(1)
>>> a
[1, [2, [3, [None]]]]
>>> a.include(4)
False
>>> a.include(2)
True
>>> a.pop()
1
>>> a.pop()
2
>>> a.pop()
3
>>> a
[None]
>>> a.include(2)
False
"""


class LinkedList():
    def __init__(self):
        self.array = [None]

    # Добавление элемента в односвязанный список. По сути сдвиг ссылки:
    # было [None] после push(x) -> [x,[None]] после push(y) -> [y, [x,[None]]]
    def push(self, value):
        self.array = [value, self.array]

    # Удаление начального элемента из односвязанного списка:
    # было [y, [x,[None]]] после pop() -> [x,[None]] после pop() -> [None]
    def pop(self):
        value = self.array[0]
        if value is None:
            return None
        self.array = self.array[1]
        return value

    # Поиск вхождения элемента в связанный список. Идем по всем элементам: О(N)
    def include(self, value):
        link = self.array
        while link[0] is not None:
            if link[0] == value:
                return True
            link = link[1]
        return False

    def __repr__(self):
        return f"{self.array}"

    def __str__(self):
        return f"<<< {self.array} >>>"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
