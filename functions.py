#!/usr/bin/python3

def main():
    testfunc(1, 3, 4, 5, 14, 145, 16, 17)

def testfunc(this, that, other, *args):
    print('This is a test function')
    print(this, that, other, args)
    for n in args: print(n, end=' ')
"""
# This will give you tuple of that value.
you can do for loop and print it if you want like this.
This is not the list, so it's immutable.
"""

if __name__ == "__main__": main()

