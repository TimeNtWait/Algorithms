"""Нумерация всех вершин по порядку уровней. Для ориентированных графов"""
from graph import Graph


def calc_numbering_vertex(input_string):
    # Формируем ориентированный граф на основе заданной строки ребер
    graph = Graph(oriented=True)
    graph.graph_from_string(input_string)

    # Ищем родительские вершины
    tops_vertexes = graph.find_root_vertex()
    visited_node = set()
    graph_numbers = {}
    for top_v in tops_vertexes:
        graph_numbers[top_v] = 0
        graph.dfs_numbering(top_v, visited_node, graph_numbers)
    return graph_numbers


if __name__ == "__main__":
    # Для формирования графа используем строку
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
    graph_numbers = calc_numbering_vertex(string)
    print(f"graph_numbers: {graph_numbers}")
