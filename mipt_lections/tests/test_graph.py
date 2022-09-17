"""Тестирование класса Graph
Тестирование производится за счет прогона алгоритмов по работе с графами:
- Алгоритм Косарайю (algo_Kosaraju_connected_components.py) - DFS
- Алгоритм Тарьяна (algo_Kosaraju_connected_components.py) - DFS
- Нумерация всех вершин по порядку уровней (numbering_vertex.py) - DFS
- Алгоритм Дейкстры (algo_Dijkstra_find_min_path.py) - BFS
- Алгоритм Флойда-Уоршелла (algo_Floyd_Warshall_find_min_path.py)

"""
import pytest
from mipt_lections.mipt_lections.graph.graph import Graph
from mipt_lections.mipt_lections.graph.algo_Kosaraju_connected_components import calc_kosaraju
from mipt_lections.mipt_lections.graph.algo_Tarjan_sort_vertexes import calc_tarjan
from mipt_lections.mipt_lections.graph.numbering_vertex import calc_numbering_vertex
from mipt_lections.mipt_lections.graph.algo_Dijkstra_find_min_path import calc_algo_dijkstra, calc_algo_dijkstra_weights
from mipt_lections.mipt_lections.graph.algo_Floyd_Warshall_find_min_path import calc_algo_floyd_warshall


def test_graph_algo_kosaraju():
    print(f"\n Test Algorithms Kosaraju")
    input_string = """A B\nC A\nB C\nB D\nD E\nE F\nF D\nG F\nG H\nH I\nI J\nJ G\nK J\n"""
    connected_components = calc_kosaraju(input_string)
    print(f"\nFind {len(connected_components)} connected components: {connected_components}")
    assert connected_components == [{'K'}, {'I', 'G', 'J', 'H'}, {'C', 'A', 'B'}, {'E', 'D', 'F'}]


def test_graph_algo_tarjan():
    print(f"\n Test Algorithms Tarjan")
    input_string = """A B\nA C\nA D\nD C\nB F\nC F\nD G\nF E\nF G\nE J\nF J\nG J\nLN D\nC KL\nD KL\nB LP\nF LP"""
    sorted_vertex = calc_tarjan(input_string)
    sorted_vertex = sorted_vertex[::-1]  # разворачиваем
    print(f"sorted_vertex: {sorted_vertex}")
    # Проверка корректности тополгической сортировки
    assert sorted_vertex.index("D") > sorted_vertex.index("A")
    assert sorted_vertex.index("KL") > sorted_vertex.index("C")
    assert sorted_vertex.index("KL") > sorted_vertex.index("D")
    assert sorted_vertex.index("LP") > sorted_vertex.index("B")
    assert sorted_vertex.index("LP") > sorted_vertex.index("F")
    assert sorted_vertex.index("F") > sorted_vertex.index("B")
    assert sorted_vertex.index("F") > sorted_vertex.index("C")
    assert sorted_vertex.index("G") > sorted_vertex.index("F")
    assert sorted_vertex.index("G") > sorted_vertex.index("D")
    assert sorted_vertex.index("E") > sorted_vertex.index("F")
    assert sorted_vertex.index("J") > sorted_vertex.index("F")
    assert sorted_vertex.index("J") > sorted_vertex.index("G")

    input_string = """A B\nA C\nC D\nB D"""
    # Проверка корректности тополгической сортировки
    sorted_vertex = calc_tarjan(input_string)
    sorted_vertex = sorted_vertex[::-1]  # разворачиваем
    print(f"sorted_vertex: {sorted_vertex[::-1]}")
    assert sorted_vertex.index("B") > sorted_vertex.index("A")
    assert sorted_vertex.index("C") > sorted_vertex.index("A")
    assert sorted_vertex.index("D") > sorted_vertex.index("B")
    assert sorted_vertex.index("D") > sorted_vertex.index("C")


def test_graph_numbering_vertex():
    print(f"\n Test Numbering Vertex")
    string = """A B\nA C\nA D\nD C\nB F\nC F\nD G\nF E\nF G\nE J\nF J\nG J\nLN D\nC KL\nD KL\nB LP\nF LP\n"""
    graph_numbers = calc_numbering_vertex(string)
    print(f"graph_numbers: {graph_numbers}")
    assert graph_numbers == {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 3, 'F': 2, 'G': 2, 'J': 3, 'KL': 2, 'LN': 0, 'LP': 2}


def test_graph_algo_dijkstra():
    print(f"\n Test Algorithms Dijkstra")
    string = """A B\nA C\nA D\nD C\nC F\nD G\nF E\nE J\nG J\nLN D\nD KL\nB LP\nF LP\n"""
    graph = Graph(oriented=True)
    graph.graph_from_string(string)

    # Проверка с конкретно заданной вершиной и с парметром сохранения пути (save_path=True)
    find_length_path = calc_algo_dijkstra(graph, root_vertex="C", save_path=True)
    print(f"find_length_path: {find_length_path}")
    assert find_length_path == {
        'C': {'C': {'len': 0, 'path': []}, 'F': {'len': 1, 'path': ['F']}, 'LP': {'len': 2, 'path': ['F', 'LP']},
              'E': {'len': 2, 'path': ['F', 'E']}, 'J': {'len': 3, 'path': ['F', 'E', 'J']}}}

    # Проверка без параметра save_path (save_path=False)
    root_length = calc_algo_dijkstra(graph, root_vertex="A")
    print(f"root_length: {root_length}")
    assert root_length == {
        'A': {'A': {'len': 0}, 'D': {'len': 1}, 'C': {'len': 1}, 'B': {'len': 1}, 'G': {'len': 2}, 'KL': {'len': 2},
              'F': {'len': 2}, 'LP': {'len': 2}, 'J': {'len': 3}, 'E': {'len': 3}}}

    # Проверка без конкретно заданной вершины параметра save_path (save_path=False)
    root_length_not_vertex = calc_algo_dijkstra(graph)
    print(f"root_length_not_vertex: {root_length_not_vertex}")
    assert root_length_not_vertex == {
        'LN': {'LN': {'len': 0}, 'D': {'len': 1}, 'G': {'len': 2}, 'KL': {'len': 2}, 'C': {'len': 2}, 'J': {'len': 3},
               'F': {'len': 3}, 'LP': {'len': 4}, 'E': {'len': 4}},
        'A': {'A': {'len': 0}, 'D': {'len': 1}, 'C': {'len': 1}, 'B': {'len': 1}, 'G': {'len': 2}, 'KL': {'len': 2},
              'F': {'len': 2}, 'LP': {'len': 2}, 'J': {'len': 3}, 'E': {'len': 3}}}

def test_graph_algo_dijkstra_weight():
    print(f"\n Test Algorithms Dijkstra Weight")
    string = """A B 1\nA C 2\nB D 3\nC D 4\n"""
    graph_weight = Graph(oriented=True, weighed=True)
    graph_weight.graph_from_string(string)

    # Проверка с конкретно заданной вершиной и с парметром сохранения пути (save_path=True)
    find_length_for_A_weight = calc_algo_dijkstra_weights(graph_weight,"A", save_path=True)
    print(f"find_length_for_A_weight : {find_length_for_A_weight}")
    assert find_length_for_A_weight == {'A': {'len': 0, 'path': []}, 'B': {'len': 1.0, 'path': ['B']}, 'C': {'len': 2.0, 'path': ['C']}, 'D': {'len': 4.0, 'path': ['B', 'D']}}


def test_graph_algo_floyd_warshall():
    print(f"\n Test Algorithms Floyd-Warshall")
    input_string = """
    A B 2
    B C 3
    A D 4
    D B 5
    """
    # Ориентированный граф
    graph = Graph(oriented=True, weighed=True)
    graph.graph_from_string(input_string)
    matrix_distance = calc_algo_floyd_warshall(graph)
    print("\nmatrix_distance for Orient graph", *matrix_distance, sep="\n")
    assert matrix_distance == [[0, 2.0, None, 4.0], [2.0, 0, 3.0, 5.0], [None, 3.0, 0, None],[4.0, 5.0, None, 0]]

    # Неориентированный граф
    graph = Graph(oriented=False, weighed=True)
    graph.graph_from_string(input_string)
    matrix_distance = calc_algo_floyd_warshall(graph)
    print("\nmatrix_distance for Not orient graph", *matrix_distance, sep="\n")
    assert matrix_distance == [[0, 2.0, 5.0, 4.0],[2.0, 0, 3.0, 5.0],[5.0, 3.0, 0, 8.0],[4.0, 5.0, 8.0, 0]]


    # TODO: добавить дополнительные алгоритмы поиска на графах https://ru.wikipedia.org/wiki/Категория:Алгоритмы_поиска_на_графах
    # TODO: реализовать Двунаправленный поиск
    # TODO: реализовать Лучевой поиск
    # TODO: Лексикографический поиск в ширину
    # TODO: Поиск в ширину
    # TODO: Поиск по критерию стоимости
    # TODO: Поиск в глубину
    # TODO: Поиск с возвратом
    # TODO: Поиск восхождением к вершине
    # TODO: Поиск с ограничением глубины
    # TODO: Поиск в глубину с итеративным углублением
    # TODO: Breadth-First-Search-Algorithm
    # TODO: Альфа-бета-отсечение
    # TODO: Метод ветвей и границ
    # TODO: Поиск по первому наилучшему совпадениюA*B*D*
    # TODO: Поиск точки переходаIDA*
    # TODO: Рекурсивный поиск по первому наилучшему совпадениюSMA*
    # TODO: Волновой алгоритм
    # TODO: Алгоритм Беллмана — Форда
    # TODO: Алгоритм Джонсона
    # TODO: Алгоритм Левита
    # TODO: Поиск по краям
    # TODO: Минимальное остовное дерево
    # TODO: Алгоритм Борувки
    # TODO: Алгоритм Прима
    # TODO: Алгоритм Краскала
    # TODO: Алгоритм Британского музея
    # TODO: Алгоритм Эдмондса
    # TODO: Обход дерева
    # TODO: Алгоритм ближайшего соседа в задаче коммивояжёра
