
# O(Fib n)


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# дерево Фибоначчи
# fib(4) -> fib(3) -> fib(2) -> fib(1)
#   |               -> fib(0)
#   |    -> fib(1)
#   |
# fib(2) -> fib(1)
#        -> fib(0)


def fibo(n):
    fib = [0, 1] + [0]*n
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[n-2]
    return fib[n]