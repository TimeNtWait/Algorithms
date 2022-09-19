"""
1028. Recover a Tree From Preorder Traversal
(1028. Восстановить дерево из обхода предварительного заказа)
https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]


"""
# TODO add comments
# TODO translate RUS->ENG


import re  # Import regular expression
from collections import deque  # Import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str):
        find_substr = re.findall(r'(-*\d+)', traversal)
        stack = []
        for i in range(len(find_substr)):
            node = find_substr[i]
            value = int(re.findall(r'(\d+)', node)[0])
            level = node.count("-")
            tree_node = TreeNode(val=value)
            # Add instance TreeNode attributes: parent and level
            tree_node.parent = None
            tree_node.level = level
            stack.append(tree_node)

        root_node = parent_node = stack.pop(0)
        self.levels = 0

        while stack:
            node = stack.pop(0)
            # Find root parent for node
            while node.level < parent_node.level:
                parent_node = parent_node.parent
            if node.level > parent_node.level:
                if not parent_node.left:
                    parent_node.left = node
                else:
                    parent_node.right = node
            elif node.level == parent_node.level:
                parent_node = parent_node.parent
                parent_node.right = node
            node.parent = parent_node
            parent_node = node
            # Update max level
            if node.level > self.levels:
                self.levels = node.level
        # Visualization tree on array
        print(self.tree_to_array(root_node))
        return root_node

    def tree_to_array(self, root_node):
        queue = deque()
        queue.append(root_node)
        keys_in_level = {0: [root_node.val]}
        while queue:
            node = queue.popleft()
            # Fill keys_in_level for each level for missing node set None
            if node.level < self.levels:
                if node.level + 1 not in keys_in_level:
                    keys_in_level[node.level + 1] = []
                if node.left:
                    queue.append(node.left)
                    keys_in_level[node.level + 1] += [node.left.val]
                else:
                    keys_in_level[node.level + 1] += [None]

                if node.right:
                    queue.append(node.right)
                    keys_in_level[node.level + 1] += [node.right.val]
                else:
                    keys_in_level[node.level + 1] += [None]
        nodes = []
        for level in range(self.levels + 1):
            # Remove last None from list nodes
            if level == self.levels:
                while keys_in_level[level][-1] is None:
                    keys_in_level[level].pop()
            for key in keys_in_level[level]:
                nodes.append(key)
        return nodes


if __name__ == "__main__":
    solution = Solution()
    traversal = "1-2--3--4-5--6--7"
    traversal = "1-2--3---4-5--6---7"
    traversal = "1-401--349---90--88"

    from line_profiler import LineProfiler
    lp = LineProfiler()
    lp_wrapper = lp(Solution().recoverFromPreorder)
    output_graph = lp_wrapper(traversal)
    lp.print_stats()


    output_graph = solution.recoverFromPreorder(traversal)
    print(f"output_graph: {output_graph}")
