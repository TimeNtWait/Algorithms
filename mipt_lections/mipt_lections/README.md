# Алгоритмы и структуры данных (курс МФТИ)

Алгоритмы и структуры, разработанные в рамках курса МФТИ "Алгоритмы и структуры данных"
(https://www.youtube.com/playlist?list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0)

Структуры данных:
- [Heap (Куча)](heap)
- [Stack (Стэк)](stack)
- [LinkedList (Односвязный список)](hash/linkedlist.py)
- [Hash (Hash-таблица)](hash/hash.py)
- [Graph (Граф)](graph/graph.py)

Алгоритмы:
- [Алгоритмы сортировки](sorting/)
Набор различных сортировок:
    - Сортировка вставкой
    - Сортировка выбором
    - Сортировка пузырьком
    - Сортировка подсчетом частот
    - Быстрая сортировкаа по методу Тони Хоара
    - Сортировка слиянием (слияние отсортированных массивов)
- [Ханойская башня](hanoi_towers.py)
- [Бинарный поиск элемента в массиве](binary_search.py)
- [Задача про короля](king.py)
- [Редакционное расстояния между строками (Расстояние Левенштейна)](compare_words.py)
- Алгоритмы по работе с графами:
    - [Алгоритм Косарайю (DFS). Поиск компонент сильной связности](graph/algo_Kosaraju_connected_components.py)
    - [Алгоритм Тарьяна (DFS). Топологическая сортировка вершин](graph/algo_Tarjan_sort_vertexes.py)
    - [Нумерация всех вершин по порядку уровней (DFS)](graph/numbering_vertex.py)
    - [Алгоритм Дейкстры (BFS). Поиска кратчайшего пути в графе](graph/algo_Dijkstra_find_min_path.py)
    - [Алгоритм Флойда-Уоршелла. Поиска кратчайшего пути в графе](graph/algo_Floyd_Warshall_find_min_path.py)
    - [Поиск кратчайшеего пути хождения шахматного Коня](chess_horse.py)

Тесты:
- Pytest для всего кода: [tests](../tests/)
- Doctest - внутри классов [Heap](heap), [Stack](stack), [LinkedList](hash/linkedlist.py), [Hash](hash/hash.py), [Graph](graph/graph.py)

