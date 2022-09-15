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


# @pytest.fixture(scope="module")
# def create_heap():
#     heap = Heap()
#     yield heap

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


def test_numbering_vertex():
    print(f"\n Нумерация вершин по порядку уровней")

    string = """A B\nA C\nA D\nD C\nB F\nC F\nD G\nF E\nF G\nE J\nF J\nG J\nLN D\nC KL\nD KL\nB LP\nF LP\n"""
    graph_numbers = calc_numbering_vertex(string)
    print(f"graph_numbers: {graph_numbers}")
    assert graph_numbers == {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 3, 'F': 2, 'G': 2, 'J': 3, 'KL': 2, 'LN': 0, 'LP': 2}

