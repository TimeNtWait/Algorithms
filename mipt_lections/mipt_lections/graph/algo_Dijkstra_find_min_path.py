"""Алгоритм Дейкстры (Dijkstra's algorithm). Поиска кратчайшего расстояния в графе
Поиск в ширину (breadth-first search, BFS)
Для обхода в ширину используется очередь (collections.deque)

Ограничение алгоритма не работает с отрицательными весами. Это можно исправить
увеличением всех весов до такого значения чтобы небыло отрицательных. Либо
использованием другого алгоритма, например Алгоритм Флойда-Уоршелла.
"""

from graph import Graph
from collections import deque


def create_graph(input_string: str):
    graph = Graph(oriented=True)
    graph.graph_from_string(input_string)
    return graph


def calc_algo_dijkstra(graph: Graph, root_vertex: str = None, save_path: bool = False):
    """
    Расчет кратчайшего расстояния от вершины root_vertex до досутпных вершин
    Используется Поиск в ширину (BFS). Используется очередь (collections.deque)

    :param graph:Graph - граф
    :param root_vertex:str - вершина для которой будет осуществлятся поиск
    расстояний до всех доступных вершин. Если параметр не задан, тогда
    будут использоваться корневые вершины, которые определяются самостоятельно
    По умолчанию None
    :param save_path: = Сохранять ли путь кратчайшего расстояния
    По умолчанию False
    :return: Словарь по искомым вершинам содержащий перечень всех доступных
    вершин с указанием расстояние "len" и пути "path" (если save_path=True)
    """
    # Если корневая вершина не задана, то определяем все верхние корневые
    if root_vertex:
        root_vertexes = [root_vertex]
    else:
        root_vertexes = graph.find_root_vertex()
        # Если корневые вершины не определены, тогда анализщируются все вершины
        if len(root_vertexes) == 0:
            root_vertexes = graph.graph.keys()
    root_length = {}
    for root in root_vertexes:
        queue = deque([root])
        length = {root: {"len": 0}}
        if save_path:
            length[root]["path"] = []
        while queue:
            parent = queue.popleft()
            for child in graph.graph[parent]:
                if child not in length:
                    length[child] = {}
                    length[child]["len"] = length[parent]["len"] + 1
                    if save_path:
                        length[child]["path"] = length[parent]["path"] + [child]
                    queue.append(child)
        root_length[root] = length
    return root_length


def calc_algo_dijkstra_weights(graph: Graph, root_vertex: str = None, save_path: bool = False):
    # алгоритм Дейкстры не может работать с отрицательными весами,
    # поэтому делаем предварительную проверку весов
    check_positive_weight(graph)
    # Если корневая вершина не задана, то определяем все верхние корневые
    if root_vertex:
        root_vertexes = [root_vertex]
    else:
        root_vertexes = graph.find_root_vertex()
        # Если корневые вершины не определены, тогда анализщируются все вершины
        if len(root_vertexes) == 0:
            root_vertexes = graph.graph.keys()
    for root in root_vertexes:
        queue = deque([root])
        root_length = {root: {"len": 0}}
        if save_path:
            root_length[root]["path"] = []
        while queue:
            parent = queue.popleft()
            for child in graph.graph[parent]:
                if child not in root_length or root_length[child]["len"] > (
                        root_length[parent]["len"] + graph.graph[parent][child]):
                    root_length[child] = {}
                    root_length[child]["len"] = root_length[parent]["len"] + graph.graph[parent][child]
                    if save_path:
                        root_length[child]["path"] = root_length[parent]["path"] + [child]
                    if child not in queue:
                        queue.append(child)
    return root_length


def check_positive_weight(graph):
    for v in graph.graph:
        for w in graph.graph[v].values():
            assert w >= 0, "Input Dijkstra's algorithm only positive weights"


if __name__ == "__main__":
    string = """A B
    A C
    A D
    D C
    C F
    D G
    F E
    E J
    G J
    LN D
    D KL
    B LP
    F LP
    """
    graph = create_graph(string)
    print(graph)
    find_length_for_C = calc_algo_dijkstra(graph, root_vertex="C", save_path=True)
    print(f"find_length_for_C: {find_length_for_C}")

    find_length_for_A = calc_algo_dijkstra(graph, root_vertex="A")
    print(f"find_length_for_A: {find_length_for_A}")

    find_length_for_top_vertex = calc_algo_dijkstra(graph)
    print(f"find_length_for_top_vertex: {find_length_for_top_vertex}")

    input_string = """A B 2
    A H 15
    B D 5
    D E 6
    B C 1
    C F 3
    C G 1
    C D 3
    D F 4
    G F 1
    F H 3
    H I 12
    D E 6
    F E 7
    E I 2"""

    graph_weight = Graph(oriented=True, weighed=True)
    graph_weight.graph_from_string(input_string)
    find_length_for_A_weight = calc_algo_dijkstra_weights(graph_weight, "A", save_path=True)
    print(f"find_length_for_A_weight : {find_length_for_A_weight}")
