#!/usr/bin/python3
import re

# There are some basic text that needs to be matched
# itsamatch
v1 = re.compile('itsamatch')
v1.match('itsamatch')

if __name__ == '__main__':
    print v1.match('itsamatch')
