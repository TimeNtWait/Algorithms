"""Двоичное дерево поиска (binary search tree, BST)"""
from collections import deque


class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.level = None

    def __repr__(self):
        return f"<< Node: key: {self.key}, value: {self.value}, parent: {self.parent.key if self.parent else None}, left: {self.left.key if self.left else None}, right: {self.right.key if self.right else None}, level: {self.level}>>"

# TODO добавить поиск по бинарному дереву
# TODO добавить удаление из бинарного дерева
# TODO добавить балансировку бинарного дерева
class BinarySearchTree():
    def __init__(self):
        # self.binary_tree = {}
        self.tree_dict: dict[Node] = {}
        self.root = None
        self.levels = None

    def add(self, key, value=0):
        # print(key)

        node = Node(key, value)
        self.tree_dict[key] = node
        # print(node.key)
        # print(node)
        # Если дерево пустое
        if not self.root:
            self.root = node.key
            node.level = 0
            self.levels = 1
        else:
            root = self.root
            while True:
                root_node = self.tree_dict[root]
                if node.key < root:
                    if root_node.left:
                        root = root_node.left.key
                    else:
                        root_node.left = node
                        self._add_node(node, root_node)
                        break
                else:
                    if root_node.right:
                        root = root_node.right.key
                    else:
                        root_node.right = node
                        self._add_node(node, root_node)
                        break

    def _add_node(self, node:Node, root_node:Node):
        node.parent = root_node
        node.level = root_node.level + 1
        if node.level > self.levels:
            self.levels = node.level

    def tree_to_string(self):
        queue = deque()
        queue.append(self.tree_dict[self.root])
        keys_in_level = {0: [self.root]}
        while queue:
            node = queue.popleft()

            # Заполнение массива вершин для каждого уровня,
            # если нет левой или правой вершины устанавливается None
            if node.level < self.levels:
                if node.level + 1 not in keys_in_level:
                    keys_in_level[node.level + 1] = []
                if node.left:
                    queue.append(node.left)
                    keys_in_level[node.level + 1] += [node.left.key]
                else:
                    keys_in_level[node.level + 1] += [None]
                if node.right:
                    queue.append(node.right)
                    keys_in_level[node.level + 1] += [node.right.key]
                else:
                    keys_in_level[node.level + 1] += [None]
        count_space = (self.levels + 1) * 20
        row_str = ""
        for level in range(self.levels + 1):
            for key in keys_in_level[level]:
                row_str += f"{key}".center(count_space // 2 ** level)
            row_str += "\n\n"
        return row_str


#
#     def __repr__(self):
#         return f"{__class__}: {self.binary_tree}"


if __name__ == "__main__":
    tree = BinarySearchTree()
    print(tree)
    for x in [7, 3, 9, 5, 4, 1, 2, 8, 6, 10, 12]:
        tree.add(key=x)
    print(tree.tree_dict)
    print(tree.tree_to_string())
#
#                 7
#         3               9
#     1       5       8       10
#        2  4   6                12
#
#
