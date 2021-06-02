"""
- быстрая сортировка(Тони Хоара)
O(N*log(N))  на случайной выборке
O(N^2) некоторые массивы может сортировать так
сортирующее действия выполняется на прямом ходу
без доп памяти
"разделяй и властвуй"

"""


def quick_sort(a):
    if len(a) <= 1:
        return
    barrier = a[0]
    l = []
    m = []
    r = []
    for x in a:
        if x < barrier:
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)

    quick_sort(l)
    quick_sort(r)

    k = 0
    for x in (l+m+r):
        a[k] = x
        k += 1

