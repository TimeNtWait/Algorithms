"""Алгоритм Дейкстры (Dijkstra's algorithm). Поиска кратчайшего расстояния в графе"""

from graph import Graph

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
