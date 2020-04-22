#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:00:08 2020

@author: marjan


Question1: Given an input string contains shirt sizes: S, M, L

Order the string to have the shirt sizes from small to large

example: "MSLLSM" -> "SSMMLL"
"""


def shirt_size(T):
    """
    IN: a str of length N
    OUT:  a str of length N
    sort the input str
    """
    str_list = list(T)
    s_count = 0
    m_count = 0
    l_count = 0
    for x in str_list:
        if x == 'S':
            s_count += 1
        elif x == 'M':
            m_count += 1
        elif x == 'L':
            l_count += 1
    
    res = ('S' * s_count) + ('M' * m_count) + ('L' * l_count)
    return res         
    
    
    
    
    
    
    
    
T = "M"
print(shirt_size(T))

