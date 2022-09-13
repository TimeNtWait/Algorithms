# Поиск максимальной длины совпадающей подпоследовательности в списках a и b
def compare_arrays(a: list, b: list):
    max_seq = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                ii = i + 1
                jj = j + 1
                seq = 1
                while ii < len(a) and jj < len(b):
                    if a[ii] == b[jj]:
                        seq += 1
                    else:
                        break
                    ii += 1
                    jj += 1
                if seq > max_seq:
                    max_seq = seq
    return max_seq

a = [1, 2, 3, 4, 5, 6, 7]
b = [3, 5, 6, 7, 4]
res = compare_arrays(a, b)
print(res)
