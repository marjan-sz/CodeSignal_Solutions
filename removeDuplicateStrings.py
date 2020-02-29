#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 22:01:27 2020

@author: marjan

Question: Remove all duplicates from an already sorted (in lexicographical order) array of strings.

Redefine the question:
    a) an array of strings is given as input/array is sorted 
    b) remove all duplicates from the array
    c) return an array of unique strings
    
Consider all possible cases:
    a) if the inputis not an array, return TypeError
    b) if the input array has integers or floats, remove them
     
Steps to solve the problem:
    a) Define a set to store unique elements of the input array
    b) For each element in the array, check if it does not exist in the set, add it
    c) Return the set
"""

def removeDuplicateStrings(inputArray):
    
    if not isinstance(inputArray, list):
        return TypeError
    
    my_set = set()
    for x in inputArray:
        if (x not in my_set) and (isinstance(x, str)):
            my_set.add(x)
    tmp = list(my_set)
    tmp.sort()
    tmp.sort(key = len)
    return tmp


inputArray = ['a', 'a', 'ab', 'acd', 'ab', 'ab', 'abc', 'abc', 'acdesg', 2, 3.4]
print(removeDuplicateStrings(inputArray))

