"""51. N-Queens
(51. Расстановка N ферзей на поле N*N)
https://leetcode.com/problems/n-queens/

Task like on 52 . N-Queens II (https://leetcode.com/problems/n-queens-ii)

Дополнение:
Окзыается, что можно довольно легко проверить покрытие ферзем диагоналей.
Все диагонали определяются либо как i+j (позитивно направленые)
либо i-j (негативно напрваленые). Например если рассчитывать значния i+j/i-j
для каждой ячейки матрицы 4*4 (0<= i,j <=3), получится:
0/0   1/-1   2/-2   3/-3
1/1   2/0    3/-1   4/-2
2/2   3/1    4/0    5/-1
3/3   4/2    5/1    6/0

Следовательно каждую диагональ можно представить либо (i+j) либо (i-j).
В данном решение это свойство не было использовано, однако его надо знать
"""

class Solution:
    # Generate closed cell on position Queen: vertical, horizontal, diagonal
    def gen_closed_cell(self, n, x, y):
        closed_cell = set()
        for i in range(n):
            closed_cell = closed_cell | {(i, y), (x, i), (x - i, y - i), (x - i, y + i), (x + i, y - i), (x + i, y + i)}
        return closed_cell

    # Recursive check set position Queen on open cell
    def combination_queens(self, available_cells, n, x, y, set_queens):
        count_combination = []
        for i in range(x, len(set_queens) + 1):
            for j in range(n):
                # if cell is open set in cell Queen and call recursive
                if (i, j) in available_cells:
                    set_queens.add((i, j))
                    if len(set_queens) == n:
                        count_combination.append(set_queens)
                        return count_combination
                    # close cells on position Queen: vertical, horizontal, diagonal
                    closed_cell = self.gen_closed_cell(n, i, j)
                    closed_cell = available_cells & closed_cell
                    available_cells = available_cells - closed_cell
                    if len(available_cells) >= n - len(set_queens):
                        count_combination += self.combination_queens(available_cells, n, i, j, set_queens.copy())
                    # open cells who were closed
                    available_cells = available_cells | closed_cell
                    set_queens.remove((i, j))
        return count_combination

    def create_output_array(self, n, count_combination):
        output_array = []
        for combo in count_combination:
            matrix = ["." * n for _ in range(n)]
            for point in combo:
                matrix[point[0]] = matrix[point[0]][:point[1]]  + "Q" + matrix[point[0]][point[1]+1:]
            output_array.append(matrix)
        return output_array

    def solveNQueens(self, n: int) -> list[list[str]]:
        if n == 1:
            return [["Q"]]
        if n <= 3:
            return []
        available_cells = set([(i, j) for i in range(n) for j in range(n)])
        count_combination = self.combination_queens(available_cells, n, 0, 0, set())

        output_array = self.create_output_array(n, count_combination)
        return output_array

import pytest


@pytest.mark.parametrize(
    "n, count_combo",
    [(1, 1), (2, 0), (3, 0), (4, 2), (5, 10), (6, 4), (7, 40), (8, 92), (9, 352)]
)
def test_count_combination_queens(n, count_combo):
    count_combination_queens = Solution().solveNQueens(n)
    assert len(count_combination_queens) == count_combo


if __name__ == "__main__":
    import time

    start_time = time.time()
    n = 4
    output_array = Solution().solveNQueens(n)
    print(f"output_array: {output_array}")
    print(f"count_combination_queens: {len(output_array)}")
    print(f"time: {time.time() - start_time}")
