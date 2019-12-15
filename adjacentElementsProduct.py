#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:30:12 2019

@author: marjan
Question:
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product
"""

def adjacentElementsProduct(inputArray):
    """
    Pseudocode:
    in: a list of int
    out: int (the largest product)
    Find the pair of adjacent elements in the input array that produce largest product
    Use Brute-force data structure:
    Iterate over the input array to find products of all adjacent elements and save in an array
    Find Max element in the product array and return
    """
    
    tmp = []
    for i in range(len(inputArray)):
        try:
            tmp.append(inputArray[i] * inputArray[i+1])
        except IndexError:
            pass
        
    return max(tmp)