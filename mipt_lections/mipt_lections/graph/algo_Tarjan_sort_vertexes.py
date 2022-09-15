"""Алгоритм Тарьяна. Топологическая сортировка
https://ru.wikipedia.org/wiki/Топологическая_сортировка
!! Важно, не путать с другим алгоритмом Тарьяна по поиску сильной связанности

Топологическая сортировка строит корректную последовательность вершин, каждая
из которых может зависеть от других, например:
Для графа {A->B},{A->С},{C->D},{B->D},
Вершины "B" и "C" зависят от "А", а "D" зависит от вершин "B" и "C", что
означает, что вершины B C немогут быть "посещены" ("выполнены") без
предварительного посещения вершины "А", а вершина "D" без вершин "B" и "C".
Топологическая сортировка обеспечивает упорядочивание вершин по их
зависимостям, т.е. в начале последовательности всегда будет вершина "A" в конце
всегда будет вершина "D", по середине в любом порядке "B" и "C"

В классической версией алгоритма используется такое понятие как раскрашивание
вершин в цвета:
- белый - вершина не посещена,
- серый - вершина посещена, но у неё есть непосещенные потомки
- черный - вершина посещена и её потомки также посещены.
Вместо этого в ф-ции dfs_sorted_vertex используется: массив (в виде множества)
посещенных вершин (для серых и черных) и массив вершин (в виде списка), которые
считаются уже отсортированными


Требование: граф должен быть ориентированным и не содержать циклов
"""
from graph import Graph


def calc_tarjan(string):
    graph = Graph(oriented=True)
    graph.graph_from_string(string)
    # Есть возможность задавать граф напрямую через присваивание
    # graph.graph = {1: {3, 4, 5}, 3: {7, 8}, 4: {8}, 5: {9}, 8: {7, 9, 42}, 7: {42}, 9: {42}, 42: {}}

    # Могут быть отдельно стоящие вершины без ребер, которые также надо
    # учитывать, поэтому необходимо сформировать полный перечень всех вершин
    all_vertex = list(set(list(graph.graph.keys()) + [v for x in graph.graph.values() for v in x]))

    visited = set()
    sorted_vertex = []
    for vertex in all_vertex:
        if vertex not in visited:
            graph.dfs_sorted_vertex(vertex, visited, sorted_vertex)
    return sorted_vertex


if __name__ == "__main__":
    input_string = """A B
    A C
    A D
    D C
    B F
    C F
    D G
    F E
    F G
    E J
    F J
    G J
    LN D
    C KL
    D KL
    B LP
    F LP
    Z1 Z2
    """
    sorted_vertex = calc_tarjan(input_string)
    print(f"sorted_vertex: {sorted_vertex[::-1]}")
    sorted_vertex = sorted_vertex[::-1]
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

    input_string = """A B
    A C
    C D
    B D"""
    # Проверка корректности тополгической сортировки
    sorted_vertex = calc_tarjan(input_string)
    print(f"sorted_vertex: {sorted_vertex[::-1]}")
    sorted_vertex = sorted_vertex[::-1]
    assert sorted_vertex.index("B") > sorted_vertex.index("A")
    assert sorted_vertex.index("C") > sorted_vertex.index("A")
    assert sorted_vertex.index("D") > sorted_vertex.index("B")
    assert sorted_vertex.index("D") > sorted_vertex.index("C")
