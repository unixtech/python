import itertools


'''
Infinite Iterators

'''

def count_example(start, step):
    counter = itertools.count(start, step)

    [ print(c) for c in counter if c <= 100 ]


count_example(100, 5)

