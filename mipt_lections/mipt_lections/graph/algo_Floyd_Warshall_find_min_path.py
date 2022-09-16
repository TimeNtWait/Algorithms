"""Алгоритм Флойда-Уоршелла (Robert Floyd/Stephen Warshall)
Поиска кратчайшего расстояния в графе.
Алгоритм определят матрицу кратчайших расстояний между всеми вершинами
Реалзация через динамическое программирование
Входной граф может быть как ориентированым так и неориентированым
Асимптотика О(N**3)

Суть алгоритма:
1. Дан граф, где "V" это все вершины графа, а N общее кол-во вершин
1. Формируется пустая матрица расстояний N*N
2. В матрице заполняются уже известные расстояния между вершинами "V"
3. Далее осуществляется расчет расстояния от вершины "i" до вершины "j" через
 вершину "k", для этого будут использоваться три цикла по всем вершинам "V"
 (отсюда асимптотика О(N**3)).
 Т.е. берем из "V" вершину "k" и начинаем проходить двумя циклами
 по "V", определяя вершины "i" и "j". Если есть такие вершины "i" и "j",
 для которых определены расстояния между "i"-"k" и "k"-"j" соответственно,
 тогда сумму расстояний между "i"-"k" и "k"-"j" заносим в ячейку
 матрицы расстояний в поле [i][j] сумму найденого расстояния, при условии, что
 предыдущее значнеие больше чем найденая сумма расстояний.

 Таким образом осуществляется проход по всем вершинам, и между любыми двумя
 вершинами "i" и "j" определяется расстояние через каждую вершину "k"
"""
from graph import Graph


def calc_algo_floyd_warshall(graph: Graph):
    # Определяем все вершины как перчень ключей словаря графа (Graph)
    # для взвешенного графа ключи словаря содержат все вершины
    V = sorted(graph.graph.keys())
    # формиование пустой матрицы N*N, где N кол-во вершин графа
    matrix = [[None] * len(V) for _ in range(len(V))]

    # Заполнение известных расстояний. Например для графа A B 2; B C 3, будет:
    #     A     B      C
    # A [0    2       None ]
    # B [None 0       3 ]
    # C [None None    0 ]
    for i, v1 in enumerate(V):
        for j, v2 in enumerate(V):
            if v2 in graph.graph[v1]:
                matrix[i][j] = graph.graph[v1][v2]
    # Производится заполнение матрицы
    # Асимптотика О(N**3).
    for k, add_vertex in enumerate(V):
        for i, v1 in enumerate(V):
            for j, v2 in enumerate(V):
                if matrix[i][k] != None and matrix[j][k] != None:
                    new_distance = matrix[i][k] + matrix[j][k]
                    if matrix[i][j] == None or matrix[i][j] > new_distance:
                        matrix[i][j] = new_distance
    return matrix


if __name__ == "__main__":
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

    graph_weight = Graph(oriented=False, weighed=True)
    graph_weight.graph_from_string(input_string)
    matrix_distance = calc_algo_floyd_warshall(graph_weight)
    print(*matrix_distance, sep="\n")
