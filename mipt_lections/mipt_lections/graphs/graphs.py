"""Класс по работе с графами
Методы
- graph_from_string(string: str) -> "Формируется ориентированый граф из строки"
- add_edge(v1, v2) -> "Добавление ребер в граф"
- reverse() -> "Формируется обратно-ориентированый граф"
- remove_vertex(vertex) -> "Удаление заданной вершины (vertex) и связанных с ней ребер из прямого и обратного графа"
- dfs_with_stack(graph, vertexes, visited_vertex, stack) -> "Поиск в глубину (Depth-first search) с сохранением стека прошедших вершин"

>>> string = "A B\\nC B\\nB C"
>>> graph = Graph(oriented=True)
>>> graph.graph_from_string(string)
>>> graph.graph == {'A': {'B'}, 'B': {'C'}, 'C': {'B'}}
True
>>> graph.reverse() == {'A': set(), 'B': {'A', 'C'}, 'C': {'B'}}
True
>>> graph.reverse_graph == {'A': set(), 'B': {'A', 'C'}, 'C': {'B'}}
True
>>> graph.add_edge("B", "G")
>>> graph.graph == {'A': {'B'}, 'B': {'C', 'G'}, 'C': {'B'}, 'G': set()}
True
>>> graph.reverse_graph == {'A': set(), 'B': {'A', 'C', 'G'}, 'C': {'B'}, 'G': set()}
True
>>> graph.remove_vertex("C")
>>> graph.graph == {'A': {'B'}, 'B': {'G'}, 'G': set()}
True
>>> graph.reverse_graph == {'A': set(), 'B': {'A', 'G'}, 'G': set()}
True
"""


class Graph():
    def __init__(self, oriented=False):
        """
        :param oriented: - ориентированный граф или нет. Влияет на формирование
        графа: если граф ориентированный - ребра добавляются в строго указанном
        порядке от вершины v1 к v2, если граф неориентированный - ребра 
        добавляются в обе стороны, как от вершины v1 к v2 так и от v2 к v1.
        Для ориентированного графа допустим расчет развернутого графа reverse()
        """
        self.graph = {}
        self.oriented = oriented
        self.reverse_graph = {}

    # Формируется ориентированый граф из строки
    def graph_from_string(self, string: str):
        for row in string.split("\n"):
            if row.strip() == "":
                continue
            vertex1, vertex2 = row.strip().split(" ")
            for v1, v2 in [(vertex1, vertex2)]:
                self.add_edge(v1, v2)

    # Добавление ребер в граф
    def add_edge(self, v1, v2):
        self._add_edge_in_graph(self.graph, v1, v2)
        # Для неориентированнлого графа ребра добавляются в обе стороны
        if not self.oriented:
            self._add_edge_in_graph(self.graph, v2, v1)
        # Добавление вершины и связанных ребер для обратного графа
        if self.reverse_graph:
            self._add_edge_in_graph(self.reverse_graph, v1, v2)

    # Добавление ребер в граф
    def _add_edge_in_graph(self, graph, v1, v2):
        if v1 in graph:
            graph[v1].add(v2)
        else:
            graph[v1] = {v2}
        if v2 not in graph:
            graph[v2] = set()

    # Формируется обратно-ориентированый граф, когда все направления векторов
    # развернуты в обратную сторону. Обратно-ориентированный граф необходим,
    # например, для реализации алгоритма Косарайю.
    def reverse(self):
        # Для неориентированного графа обратный будет равен самому себе
        if not self.oriented:
            self.reverse_graph = self.graph.copy()
        else:
            for v1 in self.graph:
                if v1 not in self.reverse_graph:
                    self.reverse_graph[v1] = set()
                for v2 in self.graph[v1]:
                    if v2 not in self.reverse_graph:
                        self.reverse_graph[v2] = set(v1)
                    else:
                        self.reverse_graph[v2].add(v1)
        return self.reverse_graph

    def remove_vertex(self, vertex):
        """Удаление заданной вершины (vertex) и связанных с ней ребер из
        прямого и обратного графа
        """
        # Удаление вершины и связанных ребер из прямого графа
        self._remove_vertex_from_graph(self.graph, vertex)
        # Удаление вершины и связанных ребер из обратного графа
        if self.reverse_graph:
            self._remove_vertex_from_graph(self.reverse_graph, vertex)

    def _remove_vertex_from_graph(self, graph, vertex):
        """Удаление заданной вершины (vertex) и связанных с ней ребер"""
        # Удаление вершины из графа
        graph.pop(vertex, None)
        # Удаление из графа ребер указывающих на удаляемую вершину
        for key in graph:
            if vertex in graph[key]:
                graph[key].remove(vertex)


    def dfs_with_stack(self, graph, vertexes, visited_vertex, stack):
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
    import doctest
    doctest.testmod()
    # string = "A B\nC B\nB C"
    # # Создаем ориентированный граф и обратный граф на основе векторов,
    # # заданных в строке string
    # graph = Graph(oriented=True)
    # graph.graph_from_string(string)
    # # graph.graph
    # # {'A': {'B'}, 'B': {'C'}, 'C': {'B'}}
    # graph.reverse()
    # # graph.graph
    # # {'A': set(), 'B': {'A', 'C'}, 'C': {'B'}}
    # print(f"graph.graph: {graph.graph}")
    # print(f"graph.reverse: {graph.reverse_graph}")
    # graph.add_edge("B", "G")
    # # graph.graph: {'A': {'B'}, 'B': {'C', 'G'}, 'C': {'B'}, 'G': set()}
    # # graph.reverse: {'A': set(), 'B': {'A', 'C', 'G'}, 'C': {'B'}, 'G': set()}
    # print(f"graph.graph: {graph.graph}")
    # print(f"graph.reverse: {graph.reverse_graph}")
    # graph.remove_vertex("C")
    # # graph.graph: {'A': {'B'}, 'B': {'G'}, 'G': set()}
    # # graph.reverse: {'A': set(), 'B': {'A', 'G'}, 'G': set()}
    # print(f"graph.graph: {graph.graph}")
    # print(f"graph.reverse: {graph.reverse_graph}")
    # # graph.graph: {'A': {'B'}, 'B': {'C', 'D'}, 'C': {'A'}, 'D': {'E'}, 'E': {'F'}, 'F': {'D'}, 'G': {'H', 'F'}, 'H': {'I'}, 'I': {'J'}, 'J': {'G'}, 'K': {'J'}}
