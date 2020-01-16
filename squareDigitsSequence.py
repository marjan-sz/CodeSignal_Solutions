#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 10:53:54 2019

@author: marjan
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
        sum = 0
        for x in arr:
            tmp = pow(x,2)
            sum += tmp
        results.append(sum)
        sum = list(str(sum))
        res = [int(x) for x in sum]
        arr = res
        if len(results) != len(set(results)):
            return len(results)

a0 = 16        
print(squareDigitsSequence(a0))

