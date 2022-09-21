"""1255. Maximum Score Words Formed by Letters
(1255 . Максимальная оценка слов, образованных буквами)
https://leetcode.com/problems/maximum-score-words-formed-by-letters/
"""
from collections import Counter


class Solution:
    # Generation all combinations
    def combinations(self, n: int, k: int) -> list:
        a = list(range(n))
        comb = a[:(k)] + [len(a)] + [0]
        k_combinations = [comb[:k]]
        i = 0
        while i < len(comb) - 1:
            if comb[i] + 1 == comb[i + 1]:
                comb[i] = a[i]
            else:
                if not i < k:
                    break
                comb[i] += 1
                k_combinations.append(comb[:k])
                i = 0
                continue
            i += 1
        return k_combinations

    # Validation word: check include word symbols in letters
    def is_validated_word(self, word, letters):
        for char in word:
            if word.count(char) > letters[char]:
                return False
        return True

    # Find max score for combination words
    def find_max_score(self, words: list[str], letters: Counter, score: dict) -> int:
        maxscore = 0
        for k in range(1, len(words) + 1):
            combinations = self.combinations(len(words), k)
            for comb in combinations:
                current_score = 0
                current_letters = letters.copy()
                for index_word in comb:
                    word = words[index_word]

                    # Validation word: check include word symbols in letters
                    if not self.is_validated_word(word, current_letters):
                        break
                    # if word validated: addition score, exclude use letters
                    for char in word:
                        current_letters[char] -= 1
                        current_score += score[char]

                if current_score > maxscore:
                    maxscore = current_score
                    # if last k-combination with all items: return maxscore
                    if k == len(words):
                        return maxscore
        return maxscore

    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        # Change score, match letters and score
        score = dict(zip([chr(l) for l in range(ord("a"), ord("z") + 1)], score))
        # Use counter for letters
        letters = Counter(letters)
        # Delete not valid word. Use words.copy() because delete word from words
        for word in words.copy():
            # Validation word: check include word symbols in letters
            if not self.is_validated_word(word, letters):
                words.remove(word)

        maxscore = self.find_max_score(words, letters, score, )
        return maxscore


import pytest
import time

@pytest.mark.parametrize(
    "words, letters, score, expected",
    [
        (["dog", "cat", "dad", "good"],
         ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
         [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         23),
        (["xxxz", "ax", "bx", "cx"],
         ["z", "a", "b", "c", "x", "x", "x"],
         [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10],
         27),
        (["daeagfh", "acchggghfg", "feggd", "fhdch", "dbgadcchfg", "b", "db", "fgchfe", "baaedddc"],
         ["a", "a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c", "c", "c",
          "c", "c", "c", "c", "c", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "e", "e", "e",
          "e", "e", "e", "e", "e", "e", "e", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "g",
          "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h",
          "h", "h"],
         [2, 1, 9, 2, 10, 5, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         298),
        (["ad", "dbacbbedc", "ae", "adbdacad", "dcdecacdcb", "ddbba", "dbcdbeaade", "aeccdcb", "bce"],
         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b",
          "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "d", "d",
          "d", "d", "e", "e", "e", "e", "e", "e"],
         [1, 8, 3, 1, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         102),
        (["cadedaecb", "dccadce", "eee", "dda", "dceeadd", "abe", "adea", "aec", "aecdbecbbe"],
         ["a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "d", "d",
          "d", "d", "d", "d", "d", "e", "e", "e", "e", "e", "e"],
         [7, 1, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         86),
    ]

)
def test_maxScoreWords(words, letters, score, expected):
    print("\nexpected:", expected)
    start_time = time.time()
    solution = Solution()
    maxscore = solution.maxScoreWords(words, letters, score)
    print(f"maxscore: {maxscore}")
    print(f"time : {time.time() - start_time}")
    assert maxscore == expected


if __name__ == '__main__':
    pytest.main(args=[__file__])
