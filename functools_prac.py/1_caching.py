from functools import cache
import timeit


@cache
def factorial(n):
    return n * factorial(n-1) if n else 1



if __name__ == "__main__":
    timer = timeit.Timer("factorial(10)", "from __main__ import factorial")
    print(f"{timer.timeit(1):.2f}")
