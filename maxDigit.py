#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 21:03:08 2019

@author: marjan
"""

def maxDigit(n):
    """
    in: integer n
    out: integer n
    1. save the input as a list of int 
    2. find max in the array
    3. return the max
    """
    arr = list(str(n)) ## list of str
    arr = [int(x) for x in arr] ## list of int
        
    return max(arr)


n = 167
print(maxDigit(n))