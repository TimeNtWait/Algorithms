"""
Проверка корректности скобочной последовательности
Реализация в двух видов проверки:
- correction_tags() - только для круглых скобок "()"
- correction_various_tags() - для круглых и квадратных скобок "[]()", легко
расширяется для любого кол-ва вида скобок, за счет использования стека

>>> correction_tags("(()())")
True
>>> correction_tags("(((())(())))(())")
True
>>> correction_tags(")(")
False
>>> correction_tags("((()((())))(())")
False
>>> correction_tags("())")
False
>>> correction_various_tags("[()]")
True
>>> correction_various_tags("[(])")
False
>>> correction_various_tags("(([]))")
True
>>> correction_various_tags("([([)]")
False
"""
from stack import Stack
import doctest


# Проверка корректности скобочной последовательности для круглых скобок "()"
def correction_tags(s: str) -> bool:
    tags = 0
    for i in range(len(s)):
        if s[i] == "(":
            tags += 1
        elif s[i] == ")":
            tags -= 1
        if tags == -1:
            return False
    if tags != 0:
        return False
    return True


# Проверка корректности скобочной последовательности для круглых и квадратных
# скобок "[]()", просто расширяется для любого кол-ва вида скобок
def correction_various_tags(s: str) -> bool:
    stack = Stack()
    for i in range(len(s)):
        if s[i] not in "[]()":
            continue
        if s[i] == "(" or s[i] == "[":
            stack.push(s[i])
        elif s[i] == ")" and stack.pop() != "(":
            return False
        elif s[i] == "]" and stack.pop() != "[":
            return False
        else:
            assert s[i] in ")]", f"Неизвестный символ, который должен был быть обработан ранее: {s[i]}"
    return stack.len() == 0


if __name__ == "__main__":
    doctest.testmod(verbose=False)

    print("Проверка скобочной последовательности для круглых скобок")
    tests = [
        ["()", True],  # 010
        ["(())", True],  # 01210
        ["()()", True],  # 01010
        ["(()())", True],  # 0121210
        ["(((())(())))(())", True],
        ["(", False],  # 1
        [")", False],  # -1
        [")(", False],  # -10
        ["(()))(", False],  # 1210-10
        ["((()((())))(())", False],
        ["())", False],  # 10-1
    ]

    for i, test in enumerate(tests):
        test_in = test[0]
        test_expecting = test[1]
        test_out = correction_tags(test_in)
        print(f"test #{i + 1} - ", "Ok" if test_expecting == test_out else "Fail",
              f"\t\t test_in: {test_in}, expect:{test_expecting}, test_out: {test_out}")

    print("Проверка скобочной последовательности для двух видов скобок")
    various_tests = [
        ["(", False],
        [")", False],
        ["[()]1", True],
        ["[(])", False],
        ["(([3]))", True],
        ["()[(1)]", True],
        ["([()]([]))", True],
        ["([([)]", False],
        ["(((())(([1]))))[([([])])]", True],
        ["(]", False],
        ["[(]", False],
        ["[]2])", False],
        [")[](", False],
        ["([3)]", False],
        ["[(])", False],
        ["((4[]])))(", False],
        ["((()((()5)))(())", False],
        ["())", False],
        ["(", False],
        ["[6", False],
        [")", False],
        [")(", False],
        ["(()))(", False],
        ["())", False],
    ]

    for i, test in enumerate(various_tests):
        test_in = test[0]
        test_expecting = test[1]
        test_out = correction_various_tags(test_in)
        print(f"test #{i + 1} - ", "Ok" if test_expecting == test_out else "Fail",
              f"\t\t test_in: {test_in}, expect:{test_expecting}, test_out: {test_out}")


# Обратная польская нотация
def polska_notation(a: list):
    """
    Рассчет выражений записанных в
    обратной польской нотации
    >>> polska_notation([1,2,"+"])
    3
    >>> polska_notation([0,2,"*"])
    0
    >>> polska_notation([1,2,"+", -1, "*"])
    -3
    >>> polska_notation([4,2,3,"+","*"])
    20
    >>> polska_notation([4,2,3,"*","+"])
    10
    >>> polska_notation([4,6,3,"-","-"])
    1
    >>> polska_notation([4,6,"-",3,"-"])
    -5
    >>> polska_notation([4,2])
    """
    stack = Stack()
    if len(a) < 3:
        return None
    for i in range(len(a)):
        if type(a[i]) == int:
            stack.push(a[i])
        elif a[i] in "+-*/":
            assert stack.len() >= 2, "размер стека меньше 2х для операции"
            y = stack.pop()
            x = stack.pop()
            # print(f"{x}{a[i]}{y}")
            res = eval(f"{x}{a[i]}{y}")
            # if stack.len() == 0 and :
            if i == len(a) - 1:
                return res
            else:
                stack.push(res)
    return None


if __name__ == "__main__":
    print("Обратная польская нотация")
    print(polska_notation([4, 2, "+"]))
