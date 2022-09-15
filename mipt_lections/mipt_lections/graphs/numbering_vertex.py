"""Нумерация всех вершин по порядку уровней. Для ориентированных графов"""
from graphs import Graph

# Для формирования графа используем строку
string = """A B
A C
A D
B E
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

# Формируем ориентированный граф на основе заданной строки ребер
graph = Graph(oriented=True)
graph.graph_from_string(string)


# Поиск в глубину (Depth-first search) и нумерация уровней
def dfs_numbering(graph, vertex, find_v, graph_numbers):
    vertex_num = graph_numbers[vertex]
    for v in graph[vertex]:
        if v not in find_v:
            find_v.add(v)
            graph_numbers[v] = vertex_num + 1
            dfs_numbering(graph, v, find_v, graph_numbers)


# Ищем родительские вершины
def find_begin_vertex(graph):
    vertexes = set(graph.keys())
    for vertex in graph:
        for child in graph[vertex]:
            if child in vertexes:
                vertexes.remove(child)
    return vertexes

if __name__ == "__main__":
    tops_vertexes = find_begin_vertex(graph.graph)
    print(f"tops_vertexes: {tops_vertexes}")
    visited_node = set()
    graph_numbers = {}
    for top_v in tops_vertexes:
        graph_numbers[top_v] = 0
        dfs_numbering(graph.graph, top_v, visited_node, graph_numbers)
    print(f"graph_numbers: {graph_numbers}")
