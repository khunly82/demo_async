from concurrent.futures import ProcessPoolExecutor
from random import randint, seed
from timeit import timeit

seed(42)
VALUES = [randint(1, 25) for _ in range(10000)]

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)


def compute1():
    result = [fibo(n) for n in VALUES]
    return(sum(result))

def compute2():
    with ProcessPoolExecutor() as pool:
        result = pool.map(fibo, VALUES)
        return(sum(result))

def main():
    print(timeit(compute1, number=1))
    print(timeit(compute2, number=1))