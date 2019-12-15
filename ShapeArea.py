#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:27:55 2019

@author: marjan
Question: 
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
A 1-interesting polygon is just a square with a side of length 1.
An n-interesting polygon is obtained by taking the n - 1-interesting polygon
and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3-
and 4-interesting polygons in the picture below.
"""

def shapeArea(n):
    """
    in: int (look at the picture)
    out: int
    Find the area of a polygon for a given n
    After examining the problem, we come up with this formula
    area[n] = (n-1)*4 + area[n-1]
    Algorithm to use: Dynamic programming (solution composed of solutions to the same problem with smaller inputs)
    We use memoization to avoid re-computing same results
    """
    ## memoization
    result = [0]*n
    ## initialize first element
    result[0] = 1
    for i in range(1, n):
        ## formula changed a bit due to the fact that Python is zero-index
        result[i] = (i+1-1)*4 + result[i-1] 
            
    return result[n-1]