"""Алгоритм Косарайю. Поиск компонент сильной связности в ориентированном графе
Algorithm Kosaraju - Find strongly connected components

https://ru.wikipedia.org/wiki/Алгоритм_Косарайю
https://habr.com/ru/post/537290/
"""
from stack import Stack
from graph import Graph


def calc_kosaraju(string: str) -> list:
    # Создаем граф и обратный граф на основе векторов заданных в строке string
    graph = Graph(oriented=True)
    graph.graph_from_string(string)
    graph.reverse()

    # Проходим поиском в глубину по графу и формируем стек связанных вершин
    stack = Stack()
    visited_vertex = set()
    for root_vertex in graph.graph:
        if root_vertex not in visited_vertex:
            graph.dfs_with_stack(root_vertex, visited_vertex, stack)

    # Формируем обратный граф
    reverse_graph = graph.reverse()
    # Проходим поиском в глубину по обрамтному графу, при этом начальные
    # вершины выбираются из сформировнного стека. Одновремнно
    visited_vertex = set()
    pre_visited_vertex = set()
    connected_components = []
    while not stack.is_empty():
        vertex = stack.pop()
        if vertex in visited_vertex:
            continue
        reverse_graph.dfs_with_stack(vertex, visited_vertex, Stack())
        connected_components.append(visited_vertex - pre_visited_vertex)
        pre_visited_vertex = set(visited_vertex)
    return connected_components


if __name__ == "__main__":
    input_string = """A B
    C A
    B C
    B D
    D E
    E F
    F D
    G F
    G H
    H I
    I J
    J G
    K J
    """
    connected_components = calc_kosaraju(input_string)
    print(f"Find {len(connected_components)} connected components: {connected_components}")
