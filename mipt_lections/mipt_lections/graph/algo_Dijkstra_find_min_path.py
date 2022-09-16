"""Алгоритм Дейкстры (Dijkstra's algorithm). Поиска кратчайшего расстояния в графе
Поиск в ширину (breadth-first search, BFS)
Для обхода в ширину используется очередь (collections.deque)
"""

from graph import Graph
from collections import deque

def create_graph(input_string: str):
    graph = Graph(oriented=True)
    graph.graph_from_string(input_string)
    return graph

def calc_algo_dijkstra(graph:Graph, root_vertex: str = None, save_path: bool = False):
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

    # BFS
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

    find_length_for_C = calc_algo_dijkstra(graph, root_vertex="C", save_path=True)
    print(f"find_length_for_C: {find_length_for_C}")

    find_length_for_A = calc_algo_dijkstra(graph, root_vertex="A")
    print(f"find_length_for_A: {find_length_for_A}")

    find_length_for_top_vertex = calc_algo_dijkstra(graph)
    print(f"find_length_for_top_vertex: {find_length_for_top_vertex}")
