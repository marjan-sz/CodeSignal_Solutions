#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:09:18 2019

@author: marjan
Question:

Given integers a and b, determine whether the following pseudocode results in an infinite loop

while a is not equal to b do
  increase a by 1
  decrease b by 1

Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.
"""

def isInfiniteProcess(a, b):
    """
    Pseudocode:
    in: two integers
    out: boolean (If the given pseudocode will never stop, return True otherwise return False)
    Check if the following pseudocode results in infinite loop
    While a is not equal to b do
    increase a by 1
    decrease b by 1
    """
    while a != b:
        a += 1
        b -= 1
        if a > b:
            return True
            break
    return False


a = isInfiniteProcess(2,6)