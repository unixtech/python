import itertools
from time import time
from functools import wraps


i = range(1, 30)
j = range(1, 30)
x = range(1, 10000)
y = range(1, 10000)


#measure timing function
def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs, **vwro):
        start = int(round(time()*1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time()*1000)) - start
            print(f"finished up the args with {end_}.")
    return _time_it


# Catalan
@measure
def catalan1(x: int, y: int, i: int, j: int) -> int:
    for a, b in itertools.product(x, x):
        # print(f"Now the conjectures are {a} {b} {c} {d}")
        if a**2 - b**3 == 1:
            e = list((a, b))
            # print(e)
        else:
            # print(a**c-b**d)
            # print('Nothing found')
            f = a + b
    print(e)



if __name__ == "__main__":
    catalan1(x, y, i, j)
