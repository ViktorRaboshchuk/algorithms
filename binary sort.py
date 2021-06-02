"""
Требование: массив отсортирован

"""


def left_bond(a, key):
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (left + right)//2
        if a[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bond(a, key):
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (left + right)//2
        if a[middle] <= key:
            left = middle
        else:
            right = middle
    return right