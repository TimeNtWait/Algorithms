"""Тестирование класса Graph
Тестирование производится за счет прогона алгоритмов по работе с графами:
- Алгоритм Косарайю (algo_Kosaraju_connected_components.py)
- Алгоритм Тарьяна (algo_Kosaraju_connected_components.py)
- Нумерация всех вершин по порядку уровней (numbering_vertex.py)

"""
import pytest
from mipt_lections.mipt_lections.graph.graph import Graph
from mipt_lections.mipt_lections.graph.algo_Kosaraju_connected_components import *
from mipt_lections.mipt_lections.graph.algo_Tarjan_sort_vertexes import *
from mipt_lections.mipt_lections.graph.numbering_vertex import *
from mipt_lections.mipt_lections.graph.algo_Dijkstra_find_min_path import *


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
