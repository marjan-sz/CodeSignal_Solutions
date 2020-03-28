#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 19:43:51 2019

@author: marjan
"""
from merge_sort import mergeSort

def makeArrayConsecutive(sequence):
#    """
#    First solution with time complexity O(n^2) 
#    in: array of int
#    out: a sorted array of int containing missing digits
#    Find a set in a way that its union with sequence contains every integer missing from the array
#    
#    1. sort the input array
#        a. use heap or merge sort (both have O(nlgn) time complexity)
#    2. create an array to store missing elements, called it missing_items
#    3. iterate over the sequence array, repeat following steps for each item in the array
#        a. use current item as min and next item as max
#        b. make a range from min and max while excluding min and max
#        c. append the result in missing_items
#    4. return missing_items array
#    """
#    mergeSort(sequence)
#    missing_items = []
#    for i in range(len(sequence)):
#        mi = sequence[i]
#        if sequence[i] != sequence[-1]: ## check if we are not at the last index
#            ma = sequence[i+1] 
#        else:
#            break ## if last index is reached break out of the for loop
#        res = [x for x in range(mi+1, ma)] ## make a range between min and max while excluding min and max
#        if res: ## if res is not empty and there are digits between min and max, then add it to the result
#            ## in python the order with which we union the arrays will be preserved in the result array, hence we do not need to sort it again
#            missing_items += res
#    return missing_items
    
    """
    Second solution with time complexity: O(2n)
    1. sort the array and call it sorted_array 
    2. create a new array called missing_items
    3. create a dictionary called it my_dict
    4. iterate over the items in the input array
    5. use the array items as the dictionary keys with value is equal to True
    6. iterate over the range from first to the last item in sorted_array
        try to access the dictionary if the key (item) exist
        if the key does not exist, append the item to the result
    7. return result
    """
    mergeSort(sequence)
    missing_items = []
    my_dict = {}
    for x in sequence:
        my_dict[x] = True
        
    for i in range(sequence[0], sequence[-1]):
        try:
            if my_dict[i]:
                pass
                
        except KeyError:
                missing_items.append(i)
    return missing_items
        

    
sequence = [6, 2, 3, 8]   
print(makeArrayConsecutive(sequence))