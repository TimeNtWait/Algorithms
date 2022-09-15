"""Алгоритм Косарайю.
Поиск компонент сильной связности (strongly connected components) в ориентированном графе.
https://ru.wikipedia.org/wiki/Алгоритм_Косарайю
https://habr.com/ru/post/537290/
"""
from stack import Stack


class Graph():
    def __init__(self):
        self.graph = {}
        self.reverse_graph = {}

    # Формируется ориентированый граф
    def graph_from_string(self, string: str):
        for row in string.split("\n"):
            if row.strip() == "":
                continue
            vertex1, vertex2 = row.strip().split(" ")
            for v1, v2 in [(vertex1, vertex2)]:
                if v1 in self.graph:
                    self.graph[v1].add(v2)
                else:
                    self.graph[v1] = {v2}
                if v2 not in self.graph:
                    self.graph[v2] = set()

    # Формируется обратно-ориентированый граф, когда все направления векторов
    # развернуты в обратную сторону. Обратно-ориентированный граф необходм
    # для реализации алгоритма Косарайю.
    def reverse(self):
        for v1 in self.graph:
            if v1 not in self.reverse_graph:
                self.reverse_graph[v1] = set()
            for v2 in self.graph[v1]:
                if v2 not in self.reverse_graph:
                    self.reverse_graph[v2] = set(v1)
                else:
                    self.reverse_graph[v2].add(v1)
        return self.reverse_graph

    def dfs(self, graph, vertexes, visited_vertex, stack):
        """Поиск в глубину (Depth-first search)
        :param vertexes: вершины по которым необходимо пробежаться
        :param visited_vertex: посещенные вершины
        """
        for v in vertexes:
            if v not in visited_vertex:
                visited_vertex.add(v)
                stack = self.dfs(graph, graph[v], visited_vertex, stack)
                stack.push(v)
        return stack


if __name__ == "__main__":
    string = """A B
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
    # Создаем граф и обратный граф на основе векторов заданных в строке string
    graph = Graph()
    graph.graph_from_string(string)
    graph.reverse()

    # Проходим поиском в глубину по графу и формируем стек связанных вершин
    stack = Stack()
    visited_vertex = set()
    for root_vertex in graph.graph:
        if root_vertex not in visited_vertex:
            stack = graph.dfs(graph.graph, root_vertex, visited_vertex, stack)

    # Проходим поиском в глубину по обрамтному графу, при этом начальные
    # вершины выбираются из сформировнного стека. Одновремнно
    visited_vertex = set()
    pre_visited_vertex = set()
    connected_components = []
    while not stack.is_empty():
        vertex = stack.pop()
        if vertex in visited_vertex:
            continue
        graph.dfs(graph.reverse_graph, vertex, visited_vertex, Stack())
        connected_components.append(visited_vertex - pre_visited_vertex)
        pre_visited_vertex = set(visited_vertex)
    print(f"Find {len(connected_components)} connected components: {connected_components}")
