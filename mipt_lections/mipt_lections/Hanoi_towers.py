"""
Ханойская башня
Задача: есть три штыря, на 1м установлено N блинов, 2ой и 3ий штыри пустые
Необходимо перенести все блины с первого штыря на 2ой, при этом можно
пользоваться третим штырем как буферным, однако нельзя ставить блины большого
размера на блины меньшего размера.
"""


def hanoy_tower(count, from_tower, to_tower, buf):
    if count == 0:
        return
    hanoy_tower(count - 1, from_tower, buf, to_tower)
    to_tower.append(from_tower.pop(-1))
    hanoy_tower(count - 1, buf, to_tower, from_tower)
    return to_tower


def calc_hanoy_tower(n):
    to_tower = hanoy_tower(n, from_tower=[i + 1 for i in range(n)], to_tower=[], buf=[])
    print(to_tower)
    return to_tower


if __name__ == "__main__":
    calc_hanoy_tower(2)
    calc_hanoy_tower(3)
    calc_hanoy_tower(4)
