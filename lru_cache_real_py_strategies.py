from functools import cache, lru_cache
import pandas as pd
import pandas


@lru_cache(maxsize=5)
def fib(n: int):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)



pd.read_csv("1.csv", sep=";", delimiter=None)


def main():
    for i in range(400):
        print(i, fib(i))
    print("done")


if __name__ == "__main__":
    main()
