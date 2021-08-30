#!/usr/bin/python3

def main():
    fh = open('lines.txt')
    for line in readfile('lines.txt'): print(line.strip())

def readfile(filename):
    fh = open(filename)
    return fh.readlines()


if __name__ == "__main__": main()
