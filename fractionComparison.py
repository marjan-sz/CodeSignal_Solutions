#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:47:20 2020

@author: marjan

Question: Compare the two given fractions.

Example

    For a = [3, 4] and b = [6, 8], the output should be
    fractionComparison(a, b) = '=';
    For a = [3, 2] and b = [2, 5], the output should be
    fractionComparison(a, b) = '>';
    For a = [3, 5] and b = [2, 3], the output should be
    fractionComparison(a, b) = '<'
    
Redefine the question:
    a) two array of int is given, each has two elements, e.g. a=[a0, a1], b=[b0, b1]
    b) find the fractions in this manner: a0/a1 and b0/b1
    c) compare these two fractions
    d) if they are equal retrun '='
    e) if first one is bigger return '>'
    f) if second one is bigger return '<'
    
Consider all possible cases:
    a) the input arrays should be lenght of two and contain integers
    
Steps to solve the problem:
    a) find the first and second fractions
    b) calculate the common denominator between two fractions
        1. multiply numinator and denominator of first fraction by the denominator of the second fraction
        2. multiply numinator and denominator of second fraction by the denominator of the first fraction
    c) compare two fractions with if statements and return the result

"""

def fractionComparison(a, b):
    """
    in: two arrays of ints
    out: a str
    """
    first_fraction = a[0]/ a[1]
    second_fraction = b[0]/ b[1]
    
    first_fraction = (a[0] * b[1]) / (a[1] * b[1])
    second_fraction = (b[0] * a[1]) / (b[1] * a[1])
    
    if first_fraction == second_fraction:
        return "="
    
    elif first_fraction > second_fraction:
        return ">"
    
    elif first_fraction < second_fraction:
        return "<"
      
    
a = [3,5]
b = [2,3]
print(fractionComparison(a,b))