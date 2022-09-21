"""Generation all combinations"""


def combinations(a: list[int], k: int):
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


if __name__ == "__main__":
    a = [0, 1, 2, 3, 4]

    for k in range(1, len(a) + 1):
        k_combinations = combinations(a, k)
        print(f"Combinations for k={k}: {k_combinations}")
