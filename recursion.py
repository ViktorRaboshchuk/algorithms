
def gen_bin(m, prefix=""):
    if m == 0:
        print(prefix)
        return
    gen_bin(m-1, prefix+"0")
    gen_bin(m-1, prefix+"1")


def generate_number(n: int, m: int, prefix=None):
    """ Генерирует все числа в n-ричной системе исчесления"""
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        generate_number(n, m-1, prefix)
        prefix.pop()


# gen_bin(3)
#
# generate_number(3, 3)


def search(x, a):
    """ищет х в а, и возвращает True если такой есть, False если нет"""

    for number in a:
        if x == number:
            return True
    return False


def generate_permutation(n: int, m: int = -1, prefix=None):
    """
    Генерация всех перестановок  n чисел в m позициях с префиксом
    """

    m = n if m == -1 else m  # по умолчанию n чисел в m позициях
    prefix = prefix or []
    if m == 0:
        print(*prefix)
        return
    for number in range(1, n+1):
        if search(number, prefix):
            continue
        prefix.append(number)
        print("append:", number, prefix)
        generate_permutation(n, m-1, prefix)
        prefix.pop()
        print("pop:", number, prefix)


generate_permutation(3)
