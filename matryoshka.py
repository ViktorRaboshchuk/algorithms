
def matryoshka(n):
    if n == 1:
        print("Min матрешка")
    else:
        print("Верх матрешки n=", n)
        matryoshka(n-1)
        print("Низ матрешки n=", n)


matryoshka(5)


def f(n: int):
    """ Алгоритм Факториал """
    assert n >=0 , "Факторил от не отрицательных чисел"
    if n == 0:
        return 1
    print("n: ", n, "f(n-1)*n: ", f(n-1)*n)
    return f(n-1)*n


def gcd(a, b):
    """ Алгоритм Эвклида"""
    return a if b == 0 else gcd(b, a % b)


res = gcd(20, 245)
print(res)


def pow(a: float, n: int):
    """ Быстрое возведение в степень"""
    if n == 0:
        return 1
    elif n % 2 == 1: # четные
        pow(a, n-1)*a
    else:            # четные
        pow(a**2, n//2)