"""Класс по работе с графами

# Переделать реверс  не как внутрениий допграф а как отдельный объект класса
# перенсти поиск топ вершин из алогоримта нумерации
# перенсти все из алогоримта Дийкстра
# перенсти все из алогоримта нумерации
# добавить тесты
# добавить описание методов
# поравить readme

Методы
- graph_from_string(string: str) -> "Формируется ориентированый граф из строки"
- add_edge(v1, v2) -> "Добавление ребер в граф"
- remove_vertex(vertex) -> "Удаление заданной вершины (vertex) и связанных с ней ребер из прямого и обратного графа"
- reverse() -> "Формируется обратно-ориентированый граф"
- dfs_with_stack(graph, vertexes, visited_vertex, stack) -> "Поиск в глубину (Depth-first search) с сохранением стека прошедших вершин"
- dfs_numbering(vertex, find_vertex, graph_numbers) -> "Поиск в глубину (Depth-first search) и нумерация уровней"
- dfs_sorted_vertex(vertex, visited, sorted_vertex) -> "Поиск в глубину (Depth-first search) Алгоритм Тарьяна. Топологическая сортировка"
- find_root_vertex() -> "Ищем родительские вершины"


>>> string = "A B\\nC B\\nB C"
>>> graph = Graph(oriented=True)
>>> graph.graph_from_string(string)
>>> graph.graph == {'A': {'B'}, 'B': {'C'}, 'C': {'B'}}
True
>>> reverse_graph = graph.reverse()
>>> reverse_graph.graph == {'A': set(), 'B': {'A', 'C'}, 'C': {'B'}}
True
>>> graph.add_edge("B", "G")
>>> graph.graph == {'A': {'B'}, 'B': {'C', 'G'}, 'C': {'B'}, 'G': set()}
True
>>> reverse_graph = graph.reverse()
>>> reverse_graph.graph == {'A': set(), 'B': {'C', 'A'}, 'G': {'B'}, 'C': {'B'}}
True
>>> graph.remove_vertex("C")
>>> graph.graph == {'A': {'B'}, 'B': {'G'}, 'G': set()}
True
>>> reverse_graph = graph.reverse()
>>> reverse_graph.graph == {'A': set(), 'B': {'A'}, 'G': {'B'}}
True
"""


class Graph():
    def __init__(self, oriented: bool = False, weighed: bool = False):
        """
        :param oriented: - ориентированный граф или нет. Влияет на формирование
        графа: если граф ориентированный - ребра добавляются в строго указанном
        порядке от вершины v1 к v2, если граф неориентированный - ребра 
        добавляются в обе стороны, как от вершины v1 к v2 так и от v2 к v1.
        Для ориентированного графа допустим расчет развернутого графа reverse()
        :param weighed: Учитываются лив графе веса
        """
        self.graph = {}
        self.oriented = oriented
        self.weighed = weighed

    # Формируется ориентированый граф из строки
    def graph_from_string(self, string: str):
        # Если указан весовой граф, то используем парсер с весами
        if self.weighed:
            self.graph_from_string_weight(string)
            return
        for row in string.split("\n"):
            if row.strip() == "":
                continue
            vertex1, vertex2 = row.strip().split(" ")
            for v1, v2 in [(vertex1, vertex2)]:
                self.add_edge(v1, v2)

    # Формируется ориентированый граф из строки
    def graph_from_string_weight(self, string: str):
        for row in string.split("\n"):
            if row.strip() == "":
                continue
            vertex1, vertex2, weight = row.strip().split(" ")
            weight = float(weight)
            for v1, v2 in [(vertex1, vertex2)]:
                self.add_edge(v1, v2, weight)

    # Добавление ребер в граф
    def add_edge(self, v1, v2, weight=None):
        self._add_edge_in_graph(v1, v2, weight)
        # Для неориентированнлого графа ребра добавляются в обе стороны
        if not self.oriented:
            self._add_edge_in_graph(v2, v1, weight)

    # Добавление ребер в граф
    def _add_edge_in_graph(self, v1, v2, weight=None):
        # Если формируем взвешанный граф, то добавляем веса в ребра
        # Для взвешанного графа ребра хранятся в словаре (dict) с записью веса
        if self.weighed:
            # Если вес для ребра не указан, тогда указываем 0
            if weight is None:
                weight = 0
            if v1 in self.graph:
                self.graph[v1][v2] = weight
            else:
                self.graph[v1] = {}
                self.graph[v1][v2] = weight
            if v2 not in self.graph:
                self.graph[v2] = {}
            # для взвешанного графа указываем расстояние вершины до самой себя,
            # даже если изначально не было задано такое расстояние
            if v1 not in self.graph[v1]:
                self.graph[v1][v1] = 0
            if v2 not in self.graph[v2]:
                self.graph[v2][v2] = 0
        # Для НЕвзвешанного графа ребра хранятся в виде множества (set)
        else:
            if v1 in self.graph:
                self.graph[v1].add(v2)
            else:
                self.graph[v1] = {v2}
            if v2 not in self.graph:
                self.graph[v2] = set()

    # Формируется обратно-ориентированый граф, когда все направления векторов
    # развернуты в обратную сторону. Обратно-ориентированный граф необходим,
    # например, для реализации алгоритма Косарайю.
    # Возвращается новый объект класса Graph()
    def reverse(self):
        # Обратный граф применим только для ориентированного графа
        if not self.oriented:
            return None
        reverse_graph = Graph()
        for v1 in self.graph:
            if v1 not in reverse_graph.graph:
                reverse_graph.graph[v1] = set()
            for v2 in self.graph[v1]:
                if v2 not in reverse_graph.graph:
                    reverse_graph.graph[v2] = set(v1)
                else:
                    reverse_graph.graph[v2].add(v1)
        return reverse_graph

    def remove_vertex(self, vertex):
        """Удаление заданной вершины (vertex) и связанных с ней ребер"""
        # Удаление вершины из графа
        self.graph.pop(vertex, None)
        # Удаление из графа ребер указывающих на удаляемую вершину
        for key in self.graph:
            if vertex in self.graph[key]:
                self.graph[key].remove(vertex)

    def dfs_with_stack(self, vertex, visited, stack):
        """
        Поиск в глубину (Depth-first search)
        Дополнительно производится занесение вершин в стек

        :param vertex: вершина по которой производится поиск в глубину
        :param visited: посещенные вершины
        :param stack: ссылка на стэк в который добавляются вершины
        :return: None
        """
        for v in vertex:
            if v not in visited:
                visited.add(v)
                self.dfs_with_stack(self.graph[v], visited, stack)
                stack.push(v)

    def dfs_sorted_vertex(self, vertex, visited, sorted_vertex):
        """Поиск в глубину (Depth-first search)
        Алгоритм Тарьяна. Топологическая сортировка
        Дополнительно производится формирование списка вершин в обратном
        топологическом порядке

        :param vertex: вершина по которой производится поиск в глубину
        :param visited: посещенные вершины
        :param sorted_vertex: ссылка на список в который добавляются вершины

        В классической версией алгоритма используется такое понятие как раскрашивание
        вершин в цвета:
        - белый - вершина не посещена,
        - серый - вершина посещена, но у неё есть непосещенные потомки
        - черный - вершина посещена и её потомки также посещены.
        Вместо этого в ф-ции dfs_sorted_vertex используется: visited_vertex для
        посещенных вершин (для серых и черных) и sorted_vertex (для черных)
        В sorted_vertex вершины заносятся по обратному топологическому порядку,
        т.е. от самого нижнего потомка до самого высокого родителя
        """
        visited.add(vertex)
        for v in self.graph[vertex]:
            if v not in visited:
                self.dfs_sorted_vertex(v, visited, sorted_vertex)
        sorted_vertex.append(vertex)

    # Поиск в глубину (Depth-first search) и нумерация уровней
    def dfs_numbering(self, vertex, find_vertex, graph_numbers):
        vertex_num = graph_numbers[vertex]
        for v in self.graph[vertex]:
            # Если нумерация меньше ранее найденой, то повторяем прогон вершины
            if v not in find_vertex or vertex_num + 1 < graph_numbers[v]:
                find_vertex.add(v)
                graph_numbers[v] = vertex_num + 1
                self.dfs_numbering(v, find_vertex, graph_numbers)

    # Ищем родительские вершины
    def find_root_vertex(self):
        vertexes = set(self.graph.keys())
        for vertex in self.graph:
            for child in self.graph[vertex]:
                if child in vertexes:
                    vertexes.remove(child)
        return vertexes

    def __str__(self):
        return f"{self.graph}"

    def __repr__(self):
        return f"{__class__}, oriented:{self.oriented}, data:{self.graph}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
