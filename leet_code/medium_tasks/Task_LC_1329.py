# https://leetcode.com/problems/sort-the-matrix-diagonally/
# 1329. Sort the Matrix Diagonally
# 1329 . Отсортируйте матрицу по диагонали

class Solution:
    def get_diagonal(self, r, c):
        list_elements = []
        while r < self.cnt_rows and c < self.cnt_cols:
            list_elements.append(self.mat[r][c])
            r += 1
            c += 1
        return list_elements

    def set_diagonal(self, r, c, list_elements):
        ind = 0
        while r < self.cnt_rows and c < self.cnt_cols:
            self.mat[r][c] = list_elements[ind]
            ind += 1
            r += 1
            c += 1
        return

    def diagonalSort(self, mat):
        self.mat = mat
        self.cnt_rows = len(mat)
        self.cnt_cols = len(mat[0])

        for i in range(self.cnt_rows):
            list_elements = self.get_diagonal(i, 0)
            list_elements.sort()
            self.set_diagonal(i, 0, list_elements)
        for i in range(self.cnt_cols):
            list_elements = self.get_diagonal(0, i)
            list_elements.sort()
            self.set_diagonal(0, i, list_elements)
        return mat


if __name__ == "__main__":
    mat = [
        [3, 3, 1, 1],
        [2, 2, 1, 2],
        [1, 1, 1, 2]
    ]
    res = Solution().diagonalSort(mat)
    print(*res,sep="\n")
