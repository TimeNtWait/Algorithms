"""Набор различных сортировок:
    - Сортировка вставкой
    - Сортировка выбором
    - Сортировка пузырьком
    - Сортировка подсчетом частот
    - Быстрая сортировкаа по методу Тони Хоара
    - Сортировка слиянием (слияние отсортированных массивов)
"""
class Sort():
    def insert_sort(self, a: list) -> list:
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

    def choice_sort(self, a):
        """ Сортировка выбором. Пробегаемся по всему массиву ищем наименьший
        элемент, который устанавливаем в начальную позицию, далее из оставшейся
        последовательсности ищем следующий наименьший элемент и ставим его на
        вторую позицию и т.д. пока не дойдем до конца.
        """
        for i in range(len(a) - 1):
            for j in range(i + 1, len(a)):
                if a[j] < a[i]:
                    a[i], a[j] = a[j], a[i]
        return a

    def bubble_sort(self, a):
        """ Сортировка пузырьковым методом.
        Суть в сверке теущего элемента со следующим, если текущий больше
        следующего, тогда происходит перестановка элементов (меньший налево,
        больший направо), и курсор свдигается к следующему индексу списка.
        Таким образом за первый проход самый большой элемент будет сдвинут в
        последнюю позицию списка, за второй проход слудющий по величине будет
        пермещен на предпоследнюю позицию и т.д.
        """
        for i in range(len(a) - 1):
            for j in range(len(a) - i - 1):
                if a[j + 1] < a[j]:
                    a[j + 1], a[j] = a[j], a[j + 1]
        return a

    def calc_freq_sort(self, a, sort_range=10):
        """ Сортировка подсчетом частот.
        Подсчитывается кол-во вхождений каждого числа в последовательность.
        После чего производиться формирование итогового массива с исходя из
        кол-ва встречаемых чисел в последовательности.
        Эффективно работает на повторяющихся числах.
        Однако имеет ограничание в виде заранее заданного кол-ва обрабатываемых
        чисел и их диапозона
        """
        f = [0] * sort_range
        for x in a:
            f[x] += 1
        a = []
        for n in range(sort_range):
            a += [n] * f[n]
        return a

    def fast_sort(self, a):
        """ Быстрая сортировкаа по методу Тони Хоара
        Суть в выборе граничащего значениия и дальнешем разбиении массива
        на три части: меньше, равным, больше выбранного значения. Далее массивы
        сортируются за счет рекурсивного вызова функции (сортировать можно любой
        удобной сортировкой N**2). После сортировки идет сложение массивов.
        """
        if len(a) <= 1:
            return a
        porog = a[0]
        lt_porog = []
        eq_porog = []
        gt_porog = []
        for x in a:
            if x < porog:
                lt_porog.append(x)
            elif x == porog:
                eq_porog.append(x)
            else:
                gt_porog.append(x)
        return self.fast_sort(lt_porog) + eq_porog + self.fast_sort(gt_porog)

    def half_sort(self, a):
        """ Сортировка слиянием (слияние отсортированных массивов)
        Массив делиться на две части, после чего каждая часть сортируется
        независимо, далее отсортированные части поэлементно сравниваются
        и формируется итоговый массив
        """
        if len(a) <= 1:
            return a
        half = len(a) // 2
        b = self.half_sort(a[:half])
        c = self.half_sort(a[half:])
        a_i = b_i = c_i = 0
        a = [0] * (len(b) + len(c))
        while c_i < len(c) and b_i < len(b):
            if b[b_i] <= c[c_i]:
                a[a_i] = b[b_i]
                b_i += 1
            else:
                a[a_i] = c[c_i]
                c_i += 1
            a_i += 1
        if c_i < len(c):
            a[a_i:] = c[c_i:]
        else:
            a[a_i:] = b[b_i:]
        return a
