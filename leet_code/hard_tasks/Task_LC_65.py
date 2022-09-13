import re
class Solution:
    def isNumber(self, s):
        """Регулярками проверяем кооректность чисел. Числа с e проверяем отдельно"""
        test_n = re.findall(r'^([\+\-]?(\.|\d+?\.)?(\d*))$', s)
        test_e = re.findall(r'^([\+\-]?(\d*)(\.)?(\d*)[eE][\+\-]?(\d+))$', s)

        if test_e == [] or (test_e[0][1] == '' and test_e[0][3] == ''):
            if test_n == [] or not re.search(r'\d', test_n[0][0] + test_n[0][1]):
                return False
        return True


if __name__ == "__main__":
    arr = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", ".0e7", "e9"]
    for item in arr:
        res = Solution().isNumber(item)
        print(f"{item} - {res}")
