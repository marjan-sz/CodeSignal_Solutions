#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:31:32 2019

@author: marjan
Question:
Given the string, check if it is a palindrome.
"""

def checkPalindrome(inputString):
    """
    Pseudocode:
    in: a non-empty string
    out: boolean (True if palindrome else False)
    Read the string backward and save it in an array
    Compare to the original string to check if it is palindrome
    """
    ## convert the string to a list of chars
    input_list = list(inputString)
    n = len(input_list)
    tmp = []
    ## iterate over a list backward
    for i in range(n-1, -1, -1):
        tmp.append(input_list[i])
    ## check if the reversed string is same as the original string
    if tmp == input_list:
        return True
    else:
        return False