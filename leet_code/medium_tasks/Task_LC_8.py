"""
String to Integer (atoi)
Реализация алогоритма перевода строки в число, при условии, что:
- строка может содержать только цифры и знаки "+", "-" вначале строки
- число не может быть меньше -2147483648 и больше 2147483647
"""
import re

MAX_INT = 2147483647
MIN_INT = -2147483648


class Solution:
    def myAtoi(self, s):
        # Обрабатываем строку через регулярные выражения
        m = re.findall(r'^\s*?([\+\-]?\d+)', s)
        if m == []:
            return 0
        str_num = m[0]
        num = int(str_num)
        if num > MAX_INT:
            return MAX_INT
        elif num < MIN_INT:
            return MIN_INT
        else:
            return num


if __name__ == "__main__":
    tests = [("words and 987", 0), ("-91283472332", MIN_INT), ("-12", -12), ("+1", 1), ("-0", 0)]
    for i, test in enumerate(tests):
        test_in, test_expected = test
        test_out = Solution().myAtoi(test_in)
        print(f"test #{i}. In: {test_in}, Expected: {test_expected}, Out: {test_out}, Test ->",
              "Ok" if test_out == test_expected else "Fail")
