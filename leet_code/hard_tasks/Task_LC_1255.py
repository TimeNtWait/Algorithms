"""1255. Maximum Score Words Formed by Letters
(1255 . Максимальная оценка слов, образованных буквами)
https://leetcode.com/problems/maximum-score-words-formed-by-letters/
"""
from collections import Counter

class Solution:

    def find_max_score(self, words: list[str], letters: list[str], score: list[int], current_score:int, maxscore:int) -> int:
        """Recursion check words"""
        if current_score > maxscore:
            maxscore = current_score
        # current_letters copy letters for store change letters array
        current_letters = letters.copy()
        # current_letters = letters
        for i in range(len(words)):
            word = list(words[i])
            # validation word
            is_valid_word = True
            # check include word symbols in current_letters
            for char in word:
                if char not in current_letters or current_letters[char] == 0 or word.count(char) > current_letters[char]:
                    is_valid_word = False
                    break
            # if word not validated - skip word
            if not is_valid_word:
                continue
            # skip word if word not validated
            word_score = 0
            # if word validated: addition score, exclude use letters, call recursion check words
            for char in word:
                # current_letters.remove(char)
                current_letters[char] -= 1
                word_score += score[char]
            current_score += word_score
            maxscore = self.find_max_score(words[:i] + words[(i + 1):], current_letters, score, current_score, maxscore)
            for char in word:
                # current_letters += list(word)
                current_letters[char] += 1
            current_score -= word_score
        return maxscore

    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        # Delete not valid word. Use words.copy() because delete word from words
        for word in words.copy():
            for char in word:
                if char not in letters or letters[char] == 0 or word.count(char) > letters[char]:
                # if char not in letters or word.count(char) > letters.count(char):
                    words.remove(word)
                    break
        # Change score, match letters and score
        score = dict(zip([chr(l) for l in range(ord("a"), ord("z") + 1)], score))

        # from line_profiler import LineProfiler
        # lp = LineProfiler()
        # lp_wrapper = lp(self.find_max_score)
        # res = lp_wrapper(words, letters, score, 0, 0)
        # lp.print_stats()
        # print(res)

        maxscore = self.find_max_score(words, letters, score, 0, 0)
        return maxscore


if __name__ == "__main__":

    solution = Solution()
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Output: 23

    # words = ["leetcode"]
    # letters = ["l", "e", "t", "e", "o", "d"]
    # score = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    # # Output: 0

    words = ["xxxz", "ax", "bx", "cx"]
    letters = ["z", "a", "b", "c", "x", "x", "x"]
    score = [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]
    # Output: 27
    #
    # words = ["daeagfh", "acchggghfg", "feggd", "fhdch", "dbgadcchfg", "b", "db", "fgchfe", "baaedddc"]
    # letters = ["a", "a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c", "c",
    #            "c", "c", "c", "c", "c", "c", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "e",
    #            "e", "e", "e", "e", "e", "e", "e", "e", "e", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f", "f",
    #            "f", "f", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "h", "h", "h", "h", "h", "h", "h",
    #            "h", "h", "h", "h", "h", "h"]
    letters = Counter(letters)
    score = [2, 1, 9, 2, 10, 5, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(words)
    words = [sorted(w) for w in words]
    print(words)
    words = sorted(words, key=(lambda s: len(s)))


    import time
    start_time = time.time()


    maxscore = solution.maxScoreWords(words, letters, score)
    print(f"maxscore: {maxscore}")
    print(f"time: {time.time() - start_time}")


