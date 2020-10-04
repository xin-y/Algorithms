#! /usr/bin/python3

import sys
import random
from a2p3 import InsertIntoTrie, DeleteFromTrie

"""
Some tests.

If you set this file to executable, and have the a2p3.py file in
the same folder, then you should be able to run this.
"""

def SearchInTrie(T, s):
    if len(s) == 0:
        # weird, should not happen
        return False

    if len(s) > 0 and len(T) == 0:
        return False

    if len(s) == 1:
        return T[ord(s[0]) - ord('a')][1]

    return SearchInTrie(T[ord(s[0]) - ord('a')][0], s[1:])

def main():
    print('Test 0:', end = ' ')
    passed = True

    T = []
    InsertIntoTrie(T, "ca")
    InsertIntoTrie(T, "cat")

    passed = passed and SearchInTrie(T, "ca")
    passed = passed and SearchInTrie(T, "cat")

    DeleteFromTrie(T, "csfsfesewfw")

    passed = passed and (not SearchInTrie(T, "csfsfesewfw"))
    passed = passed and SearchInTrie(T, "ca")
    passed = passed and SearchInTrie(T, "cat")

    DeleteFromTrie(T, "ca")

    passed = passed and (not SearchInTrie(T, "ca"))
    passed = passed and SearchInTrie(T, "cat")

    DeleteFromTrie(T, "cat")

    passed = passed and (not SearchInTrie(T, "ca"))
    passed = passed and (not SearchInTrie(T, "cat"))

    if passed:
        print('Passed')
    else:
        print('Failed')

    print('Test 1:', end = ' ')
    passed = True

    T = []
    InsertIntoTrie(T, "ca")
    InsertIntoTrie(T, "cat")

    passed = passed and SearchInTrie(T, "ca")
    passed = passed and SearchInTrie(T, "cat")

    DeleteFromTrie(T, "ca")

    passed = passed and (not SearchInTrie(T, "ca"))
    passed = passed and SearchInTrie(T, "cat")

    DeleteFromTrie(T, "cat")

    passed = passed and (not SearchInTrie(T, "ca"))
    passed = passed and (not SearchInTrie(T, "cat"))

    if passed:
        print('Passed')
    else:
        print('Failed')

    print('Test 2:', end = ' ')

    T = []
    InsertIntoTrie(T, "hello")
    InsertIntoTrie(T, "world")

    if SearchInTrie(T, "hello") and SearchInTrie(T, "world") and not SearchInTrie(T, "alien"):
        print('Passed')
    else:
        print('Failed')

    print('Test 3:', end = ' ')

    DeleteFromTrie(T, "hello")
    DeleteFromTrie(T, "world")

    if T == []:
        print('Passed')
    else:
        print('Failed')

    print('Test 4:', end = ' ')
    s = set()
    nstrings = random.randint(100, 1000)
    for i in range(nstrings):
        slen = random.randint(5, 200)
        thisstr = ""
        for j in range(slen):
            c = chr(random.randint(0, 25) + ord('a'))
            thisstr = thisstr + str(c)
        s.add(thisstr)

    l = list(s)
    halflen = len(l)//2
    quarterlen = len(l)//4
    T = []
    for i in range(halflen):
        InsertIntoTrie(T, l[i])

    passed = True
    for i in range(halflen):
        passed = passed and SearchInTrie(T, l[i])

    for i in range(halflen, len(l)):
        passed = passed and (not SearchInTrie(T, l[i]))

    for i in range(quarterlen, halflen):
        DeleteFromTrie(T, l[i])

    for i in range(quarterlen):
        passed = passed and SearchInTrie(T, l[i])

    for i in range(quarterlen, len(l)):
        passed = passed and (not SearchInTrie(T, l[i]))

    if passed:
        print('Passed')
    else:
        print('Failed')


if __name__ == '__main__':
    main()
