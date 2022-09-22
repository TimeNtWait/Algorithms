"""52. N-Queens II
(52 . Расстановка N ферзей на поле N*N)
https://leetcode.com/problems/n-queens-ii

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
        count_combination = 0
        for i in range(x, set_queens + 1):
            for j in range(n):
                # if cell is open set in cell Queen and call recursive
                if (i, j) in available_cells:
                    set_queens += 1
                    if set_queens == n:
                        return count_combination + 1
                    # close cells on position Queen: vertical, horizontal, diagonal
                    closed_cell = self.gen_closed_cell(n, i, j)
                    closed_cell = available_cells & closed_cell
                    available_cells = available_cells - closed_cell
                    if len(available_cells) >= n - set_queens:
                        count_combination += self.combination_queens(available_cells, n, i, j, set_queens)
                    # open cells who were closed
                    available_cells = available_cells | closed_cell
                    set_queens -= 1
        return count_combination

    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        if n <= 3:
            return 0
        available_cells = set([(i, j) for i in range(n) for j in range(n)])
        count_combination = self.combination_queens(available_cells, n, 0, 0, 0)
        return count_combination


import pytest


@pytest.mark.parametrize(
    "n, count_combo",
    [(1, 1), (2, 0), (3, 0), (4, 2), (5, 10), (6, 4), (7, 40), (8, 92), (9, 352)]
)
def test_count_combination_queens(n, count_combo):
    count_combination_queens = Solution().totalNQueens(n)
    assert count_combination_queens == count_combo


if __name__ == "__main__":
    import time

    start_time = time.time()
    n = 9
    count_combination_queens = Solution().totalNQueens(n)
    print(f"count_combination_queens: {count_combination_queens}")
    print(f"time: {time.time() - start_time}")
