import pytest
# class Sort():
def insert_sort(a):

	""" Сортировка вставкой.
	Суть: Сортировка ведется начиная с левой стороны последовательности.
	1ый элемент берется как начальный элемент остортированной
	последовательности,	2ой элемент будет сравнен с первым и если он
	будет меньше 1го то занимает место слева становясь первым по счету,
	иначе остается вторым по счету.	Далее 3ий элемент сравнивается с
	предудущими и т.д.
	Т.е. начиная со второго элемента производится проверка каждого
	элемента с уже отсортированной последовательностью слева, и
	если слева есть элемент больше по значению, тогда меняем их местами.
	"""
	for i in range(1, len(a)):
		tmp = i
		# Пока элемент с индексом tmp (i) меньше предыдущего и
		# tmp еще не достиг левой границы тогда производим замену
		# элемента tmp на предудущий, т.е. сдвигаем элемент влево
		while tmp > 0 and a[tmp - 1] > a[tmp]:
			a[tmp - 1], a[tmp] = a[tmp], a[tmp - 1]
			tmp -= 1
	return a
#
#
# def choice_sort(a):
#     """ Сортировка выбором.
# 	Вход: массив чисел
# 	Выход отсортированный по возрастанию массив
# 	"""
#     for i in range(len(a) - 1):
#         for j in range(i + 1, len(a)):
#             if a[j] < a[i]:
#                 a[i], a[j] = a[j], a[i]
#     return a
#
#
# def bubble_sort(a):
#     """ Сортировка пуырьковым методом.
# 	Вход: массив чисел
# 	Выход отсортированный по возрастанию массив
# 	"""
#     for i in range(len(a) - 1):
#         for j in range(len(a) - i - 1):
#             if a[j + 1] < a[j]:
#                 a[j + 1], a[j] = a[j], a[j + 1]
#     return a
#
#
# def calc_freq_sort(a):
#     """ Сортировка подсчетом частот.
# 	Вход: массив чисел
# 	Выход отсортированный по возрастанию массив
# 	"""
#     f = [0] * 10
#     for x in a:
#         f[x] += 1
#     a = []
#     for n in range(10):
#         a += [n] * f[n]
#     return a
#
#
# def fast_sort2(a):
#     """ Быстрая сортировкаа по методу Тони Хоара
# 	Суть в выборе граничащего значениия и
# 	дальнешем разбиении массива на три части:
# 	меньше, равным, больше выбранного начения
# 	Далее работа подмассвами любой удобной сортировкой N**2
# 	"""
#     porog = a[0]
#     lt_porog = []
#     eq_porog = []
#     gt_porog = []
#     for i in range(len(a)):
#         if a[i] < porog:
#             lt_porog.append(a[i])
#         elif a[i] == porog:
#             eq_porog.append(a[i])
#         else:
#             gt_porog.append(a[i])
#     return calc_freq_sort(lt_porog) + eq_porog + bubble_sort(gt_porog)
#
#
# def fast_sort(a):
#     """ Быстрая сортировкаа по методу Тони Хоара
# 	рекурсия
# 	"""
#     if len(a) <= 1:
#         return a
#     porog = a[0]
#     lt_porog = []
#     eq_porog = []
#     gt_porog = []
#     for x in a:
#         if x < porog:
#             lt_porog.append(x)
#         elif x == porog:
#             eq_porog.append(x)
#         else:
#             gt_porog.append(x)
#     return fast_sort(lt_porog) + eq_porog + fast_sort(gt_porog)
#
#
# def half_sort1(a):
#     """ Сортировка слиянием (слияние отсортированных массивов)
# 	Массив делиться на две части и
# 	после ччего каждая сортируется независимо
# 	далее отсортированные части поэлементно сравниваются
# 	и формируется итоговый массив
# 	"""
#     half = len(a) // 2
#     b = calc_freq_sort(a[:half])
#     c = bubble_sort(a[half:])
#     b_i = 0
#     c_i = 0
#     a = []
#     while c_i < len(c) or b_i < len(b):
#         if c_i >= len(c) or (b_i < len(b) and b[b_i] < c[c_i]):
#             a.append(b[b_i])
#             b_i += 1
#         else:
#             a.append(c[c_i])
#             c_i += 1
#     return a
#
#
# def half_sort2(a):
#     """ Сортировка слиянием (слияние отсортированных массивов)
# 	Массив делиться на две части и
# 	после ччего каждая сортируется независимо
# 	далее отсортированные части поэлементно сравниваются
# 	и формируется итоговый массив
# 	"""
#     half = len(a) // 2
#     b = calc_freq_sort(a[:half])
#     c = bubble_sort(a[half:])
#     b_i = 0
#     c_i = 0
#     a = [0] * (len(b) + len(c))
#     for i in range(len(a)):
#         if c_i >= len(c) or (b_i < len(b) and b[b_i] <= c[c_i]):
#             a[i] = b[b_i]
#             b_i += 1
#         else:
#             a[i] = c[c_i]
#             c_i += 1
#     return a
#
#
# def half_sort(a):
#     """ Сортировка слиянием (слияние отсортированных массивов)
# 	Массив делиться на две части и
# 	после ччего каждая сортируется независимо
# 	далее отсортированные части поэлементно сравниваются
# 	и формируется итоговый массив
# 	"""
#     half = len(a) // 2
#     b = calc_freq_sort(a[:half])
#     c = bubble_sort(a[half:])
#     a_i = b_i = c_i = 0
#     a = [0] * (len(b) + len(c))
#     while c_i < len(c) and b_i < len(b):
#         if b[b_i] <= c[c_i]:
#             a[a_i] = b[b_i]
#             b_i += 1
#         else:
#             a[a_i] = c[c_i]
#             c_i += 1
#         a_i += 1
#     if c_i < len(c):
#         a[a_i:] = c[c_i:]
#     else:
#         a[a_i:] = b[b_i:]
#     # a[a_i:] = c[c_i:]
#     # a[a_i:] = b[b_i:]
#     return a
#
#
# def merge_sort(a):
#     """ Сортировка слиянием (слияние отсортированных массивов)
# 	Через рекурсию
# 	"""
#     if len(a) <= 1:
#         return a
#     half = len(a) // 2
#     b = merge_sort(a[:half])
#     c = merge_sort(a[half:])
#     a_i = b_i = c_i = 0
#     a = [0] * (len(b) + len(c))
#     while c_i < len(c) and b_i < len(b):
#         if b[b_i] <= c[c_i]:
#             a[a_i] = b[b_i]
#             b_i += 1
#         else:
#             a[a_i] = c[c_i]
#             c_i += 1
#         a_i += 1
#     if c_i < len(c):
#         a[a_i:] = c[c_i:]
#     else:
#         a[a_i:] = b[b_i:]
#     # a[a_i:] = c[c_i:]
#     # a[a_i:] = b[b_i:]
#     return a
#
#
# def test_insert_sort(sort_func):
#     print(f"Type sort: {sort_func.__name__}")
#     print(f"Type sort DOC: {sort_func.__doc__}")
#
#     test_data = [
#         [[3, 2, 5, 6, 3, 7], [2, 3, 3, 5, 6, 7]],
#         [[4, 9, 0, 3], [0, 3, 4, 9]],
#         [[1, 1, 2, 0], [0, 1, 1, 2]],
#     ]
#     for t_data in test_data:
#         a1 = t_data[0]
#         a1 = sort_func(a1)
#         print("test 1 - ", end="")
#         print("Ok" if a1 == t_data[1] else "Fail")
#
#
# types = [insert_sort, choice_sort, bubble_sort, calc_freq_sort, fast_sort, half_sort, merge_sort]
# for type_s in types:
#     test_insert_sort(type_s)
#
# print("_" * 10)
#
#
#
