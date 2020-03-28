#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:08:39 2019

@author: marjan

Question: Determine if it is possible to sort an array by reversing one of its contiguous subarrays.

Example: input array: inputArray = [-1, 5, 4, 3, 2, 8] --> True
                      inputArray = [1, 3, 2, 5, 4, 6]  --> False
                      
Redefine the question:
    1) given an input array of integers
    2) find all contiguous subarrays
    3) check if the array can be sorted by reversing one of these subarray
        a) if can be sorted return True
        b) otherwise return False
    
Cosider all possible cases:
    1) if the input array has anything other than integer return False
    2) if the input array contains more than one subarray which can be reversed to sort the array, return False
    3) what if there are repeated elements in the list? return False
    
Steps to solve the problem:
    1) the initial array is not sorted (input condition)
    2) find all continous sub-arrays and their reverse orders in the original array
        a) use nested for loop to generate sub-arrays
        b) if a sub-array length is more than 1 and its reverse order is sorted, append it to the sub-array-list
    3) insert each item in the sub-array-list into the original array one by one
        a) find min and max in the reversed sub-array
        b) find their corresponding match index (from max to min) in the original array
        c) replace the sub-array with the corresponding array elements based on their indexes
        d) if the array gets sorted, return true
        e) else return false
"""



def reverseToSort(inputArray):
    """
    in: array of ints
    out: boolean (True or False)
    Check if it is possible to sort the array by reversing one of its continous sub-arrays
    """
    if len(list(set(inputArray))) != len(inputArray):
        return False
        
    subarray_list = []
    ## find all sub-arrays
    for i in range(len(inputArray)):
        for j in range(i+1, len(inputArray)):
            tmp = inputArray[i:j+1]
            ## reverse the sub-array
            reverse_tmp = tmp[::-1]
            ## if it has at least two elements and is sorted, append it to the list
            if (len(reverse_tmp) > 1) and (reverse_tmp == sorted(reverse_tmp)):
                subarray_list.append(reverse_tmp)
                
    ## if there is any syb-array with above conditions         
    if subarray_list != []:
        ## sort it based on length in Ascending order
        subarray_list.sort(key= len)
        ## find the longest sub-array
        x = subarray_list[-1]
        ## find its length
        length = len(x)
        ## find the sub-array equivalent in the original array to determine indexes
        for index in range(0, len(inputArray)):
            ## replace the sub-array with reversed order
            if inputArray[index: index+length] == x[::-1]:
                inputArray[index: index+length] = x
    print(inputArray)
    ## if the original array is sorted after this change, return True            
    if inputArray == sorted(inputArray):
        return True
    else:
        return False
        
        
        
        
"""
subarray_list = []
   
    for i in range(len(inputArray)):
        for j in range(i+1, len(inputArray)):
            tmp = inputArray[i:j+1]
            reverse_tmp = tmp[::-1]
            if (len(reverse_tmp) > 1) and (reverse_tmp == sorted(reverse_tmp)):
                subarray_list.append(reverse_tmp)
                
    subarray_list.sort(key= len)
    x = subarray_list[-1]
    x_min = min(x)
    x_max = max(x)
    index_min = inputArray.index(x_min)
    index_max = inputArray.index(x_max)
    inputArray[index_max: index_min+1] = x
    if inputArray == sorted(inputArray):
        return True
    else:
        return False
                

"""

                
    
inputArray = [2, 3, 2, 4] ##[-1, 5, 4, 3, 2, 8]
print(reverseToSort(inputArray))

