"""1402. Reducing Dishes
(1402 . Уменьшение блюд)
https://leetcode.com/problems/reducing-dishes/
"""


class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction = sorted(satisfaction)
        if satisfaction[-1] <= 0:
            return 0
        maxscore = 0
        while satisfaction:
            sum_score = 0
            for i, dishe in enumerate(satisfaction):
                sum_score += dishe * (i + 1)
            if sum_score > maxscore:
                maxscore = sum_score
            elif sum_score < maxscore and maxscore > 0:
                return maxscore
            satisfaction.pop(0)
        return maxscore


if __name__ == "__main__":
    # satisfaction = [4,3,2]
    # satisfaction = [-1,-4,-5]
    satisfaction = [-1, -8, 0, 5, -9]
    maxscore = Solution().maxSatisfaction(satisfaction)
    print(f"maxscore: {maxscore}")
