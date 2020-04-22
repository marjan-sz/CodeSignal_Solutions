#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 10:53:54 2019

@author: marjan

Question: Consider a sequence of numbers a0, a1, ..., an, in which an element is equal to the sum of squared digits of the previous element.
The sequence ends once an element that has already been in the sequence appears again.

For a0 = 16, the output should be
squareDigitsSequence(a0) = 9.

Here's how elements of the sequence are constructed:

    a0 = 16
    a1 = 12 + 62 = 37
    a2 = 32 + 72 = 58
    a3 = 52 + 82 = 89
    a4 = 82 + 92 = 145
    a5 = 12 + 42 + 52 = 42
    a6 = 42 + 22 = 20
    a7 = 22 + 02 = 4
    a8 = 42 = 16, which has already occurred before (a0)


Given the first element a0, find the length of the sequence.

"""

def squareDigitsSequence(a0):
    """
    in: integer
    out: integer (length of the sequence)
    1. save the input as the list of integers in an array
    2. square items in the array and find the sum
    3. save the result as the list of int
    4. save the input and results in each round in an array (results)
    5. repeat 2 and 3 until the output is same as one of the items in the results 
    6. return length of the results array
    """
    arr = list(str(a0))
    arr = [int(x) for x in arr]
    
    results = [a0]
    flag = True
    while flag:
        sums = 0
        for x in arr:
            tmp = pow(x,2)
            sums += tmp
        results.append(sums)
        sums = list(str(sums))
        res = [int(x) for x in sums]
        arr = res
        if len(results) != len(set(results)):
            return len(results)

a0 = 16        
print(squareDigitsSequence(a0))

