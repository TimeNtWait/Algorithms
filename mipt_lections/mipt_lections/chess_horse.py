"""Поиск кратчайшеего пути хождения шахматного Коня
Поиск в ширину (breadth-first search, BFS)
Для обхода в ширину используется очередь (collections.deque)
В качестве BFS алгоритма будет использован алгоритм Дейкстры

Варинаты ходов шахматного Коня варьируются от 2 (если Конь в углу
шахматной доски и ограничен в движении) до 8 (если Конь в центре доски)

Задача: найти минимальное кол-во ходов Конем от одной клетки до другой
Для решения будет использоваться Поиск в ширину BFS и алгоритм Дейкстры
"""
from mipt_lections.mipt_lections.graph.algo_Dijkstra_find_min_path import *


def create_graph_chess():
    graph = Graph()
    litters = list("abcdefgh")
    for i in range(1, 9):
        for j in range(len(litters)):
            parent = f"{litters[j]}{i}"
            childs = set()
            if j > 0:
                if i > 2:
                    childs.add(f"{litters[j - 1]}{i - 2}")
                if i < 7:
                    childs.add(f"{litters[j - 1]}{i + 2}")
            if j < 7:
                if i > 2:
                    childs.add(f"{litters[j + 1]}{i - 2}")
                if i < 7:
                    childs.add(f"{litters[j + 1]}{i + 2}")
            if j > 1:
                if i > 1:
                    childs.add(f"{litters[j - 2]}{i - 1}")
                if i < 7:
                    childs.add(f"{litters[j - 2]}{i + 1}")
            if j < 6:
                if i > 1:
                    childs.add(f"{litters[j + 2]}{i - 1}")
                if i < 7:
                    childs.add(f"{litters[j + 2]}{i + 1}")
            for child in childs:
                graph.add_edge(parent, child)
    return graph


if __name__ == "__main__":
    # Формируем граф соответствующий возможным ходам коня из каждой ячейки
    graph = create_graph_chess()

    # Производим поиск кратчайшего пути через алгоритм
    start_cell = "d4"
    search_cell = "f2"
    find_length_path = calc_algo_dijkstra(graph, root_vertex=start_cell, save_path=True)
    find_path = find_length_path[start_cell][search_cell]
    print(f"from {start_cell} to: {search_cell} - len:{find_path['len']}, path:{find_path['path']}")
