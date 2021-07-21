'''
def f1():
    print('called f1')

def f2(f):
    f()


f2(f1)

# print(f1)
F1 is an object & We can pass it around


def f1(func):
    def wrapper():
        print('started')
        func()
        print('Ended')
    return wrapper


def f():
    print('Hello')


f = f1(f)

f()


'''

def f1(func):
    def wrapper(*args, **kwargs):
        print('started')
        val = func(*args, **kwargs)
        print('ended')
        return val

    return wrapper

def f2(func):
    def wrap(*args, **kwargs):
        print('started func2')
        val = func(*args, **kwargs)
        print('end')
        return val

    return wrap


@f1
def f(a: int = 4, b: int = 9):
    a = 3
    return a + b


print(f(a=5, b=9))
