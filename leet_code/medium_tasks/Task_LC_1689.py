# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# 1689 . Разбиение на минимальное количество десятичных двоичных чисел
class Solution:

    # Простое решение
    def minPartitions(self, n):
        return max(str(n))

    # Замудренное решение
    # def minPartitions(self, n):
    #     str_n = str(n)
    #     size = len(str_n)
    #     matrix = np.zeros((size,9))
    #     for i in range(size):
    #         matrix[i][:int(str_n[i])] = 1
    #     cnt = 0
    #     for num in matrix.T:
    #         if sum(num) > 0:
    #             cnt += 1
    #     return cnt


if __name__ == "__main__":
    res = Solution().minPartitions(27346209830709182346)
    print(res)

