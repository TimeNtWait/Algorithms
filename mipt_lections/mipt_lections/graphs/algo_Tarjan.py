"""Алгоритм Тарьяна. Поиск компоненты сильной связности
Топологическая сортировка вершин
Требование: граф должен быть ориентированным и не содержать циклов
"""
from graphs import Graph


def dfs_sorted_vertex(graph, vertex, visited, sorted_vertex):
    visited.add(vertex)
    for v in graph[vertex]:
        if v not in visited:
            dfs_sorted_vertex(graph, v, visited, sorted_vertex)
    sorted_vertex.append(vertex)


if __name__ == "__main__":
    string = """A B
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
    """
    graph = Graph(oriented=True)
    graph.graph_from_string(string)
    # Есть возможность задавать граф напрямую через присваивание
    # graph.graph = {1: {3, 4, 5}, 3: {7, 8}, 4: {8}, 5: {9}, 8: {7, 9, 42}, 7: {42}, 9: {42}, 42: {}}

    all_vertex = list(graph.graph.keys())
    for x in graph.graph.values():
        for v in x:
            all_vertex.append(v)
    all_vertex = list(set(all_vertex))

    visited = set()
    sorted_vertex = []

    for vertex in all_vertex:
        if vertex not in visited:
            dfs_sorted_vertex(graph.graph, vertex, visited, sorted_vertex)
    print(f"sorted_vertex: {sorted_vertex[::-1]}")
