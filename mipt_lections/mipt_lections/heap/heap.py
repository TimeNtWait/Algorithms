"""Модуль реализации Кучи heap (Структура данных типа дерево)
https://ru.wikipedia.org/wiki/Куча_(структура_данных)
>>> heap = Heap()
>>> heap.levels()
0
>>> heap.push(7)
>>> heap.levels()
1
>>> heap.push(8)
>>> heap.push(14)
>>> heap.push(5)
>>> heap.push(6)
>>> heap.levels()
3
>>> heap.len()
5
>>> print(heap)
_____
level: 1, nodes (0-0): [14]
level: 2, nodes (1-2): [7, 8]
level: 3, nodes (3-6): [5, 6]
>>> heap.pop()
14
>>> print(heap)
_____
level: 1, nodes (0-0): [8]
level: 2, nodes (1-2): [7, 6]
level: 3, nodes (3-6): [5]
"""
import math


class Heap():
    def __init__(self):
        self.heap = []

    def levels(self):
        """Высота кучи: количество """
        if self.is_empty():
            return 0
        else:
            levels = math.ceil(math.log(len(self.heap) + 1, 2))
            return levels

    def is_empty(self):
        return len(self.heap) == 0

    def len(self):
        return len(self.heap)

    def get_parent_id(self, child_id):
        parent_id = (child_id - 1) // 2
        return parent_id

    def get_childs_id(self, parent_id):
        child1_id = parent_id * 2 + 1
        child2_id = parent_id * 2 + 2
        if child1_id >= len(self.heap):
            return []
        elif child2_id >= len(self.heap):
            return [child1_id]
        else:
            return [child1_id, child2_id]

    def push(self, item):
        """Добавляем элемент в кучу. После добавления нового элемента идёт
        проверка корректности кучи (расположение больших и меньших элементов)
        """
        self.heap.append(item)
        current_index = self.len() - 1
        if current_index > 0:
            self.check_heap(current_index)

    def check_heap(self, current_index):
        """Проверка корректности кучи для выбранного элемента.
        Под корректностью понимается условие иерархии элемнтов по значению.
        Т.е. для каждого элемента: родитель больше, а потомок меньше по значению

        Если значение элемента больше родителя, то дочерний элемент
        меняется с родительским и процедура проверки для элемента продолжается,
        но уже с родительским элементом более верхнего уровня.
        """
        current_value = self.heap[current_index]
        parent_id = self.get_parent_id(current_index)
        if current_value > self.heap[parent_id]:
            self.heap[current_index], self.heap[parent_id] = self.heap[parent_id], self.heap[current_index]
        if parent_id != 0:
            self.check_heap(parent_id)

    def __str__(self):
        """Отображение кучи в виде уровней и всех элемнтов кучи на каждом уровне
        """
        res_str = "_" * 5
        for l in range(self.levels()):
            res_str += f"\nlevel: {l + 1}, nodes ({2 ** l - 1}-{(2 ** l - 1) * 2}): {self.heap[(2 ** l - 1):(2 ** l - 1) * 2 + 1]}"
        return res_str

    def pop(self):
        """Возвращается первый элемент кучи (максимальный). Данный элемент
        удаляется из кучи и далее идет сдвиг всей кучи на 1 элемент, с учетом
        проверки взаимного расположения элементов в кучи: большие по значению
        элементы находятся выше по иерархии элементов с меньшими значениями"""
        parent_id = 0
        pop_item = self.heap[parent_id]
        childs = self.get_childs_id(parent_id)
        while len(childs) > 0:
            if len(childs) == 0:
                self.heap.pop(-1)
                return None
            elif len(childs) == 1:
                id_max_child = childs[0]
            elif self.heap[childs[0]] > self.heap[childs[1]]:
                id_max_child = childs[0]
            else:
                id_max_child = childs[1]
            self.heap[parent_id] = self.heap[id_max_child]
            parent_id = id_max_child
            childs = self.get_childs_id(id_max_child)
        self.heap[id_max_child] = self.heap[-1]
        self.heap.pop(-1)
        return pop_item


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
