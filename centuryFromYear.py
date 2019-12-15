#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:32:46 2019

@author: marjan
Question:
Given a year, return the century it is in.
The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
"""

import math

def centuryFromYear(year):
    """
    Pseudocode:
    in: an integer determine a year
    out: an integer determine the century the year is in
    example: 1-100 --> first century and 101-200 --> second century
    Divide the year by 100. Round it up to the nearest integer to find the century
    """
    century = math.ceil(year/100)
    return century