#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:24:07 2020

@author: marjan

A) Redefining the question:

we are having two string as input, check if they are anagrams and if they are return true, otherwise return false
Anagram: two words are anagrams if they both have the exact same set of characters but in a different order, we can have space anywhere in between characters


B) Clarify all possible cases (NEVER ASSUME ANYTHING)

-> Return false if one of arguments is not string
-> Return true if both inputs are empty space
-> Return true if we have integers and floats in the strings -> ".24", "4.2" and "42." can be counted as anagrams
-> What to do with capital letters? either upper case or lower case, we consider them as part of the anagram, change all to lower case
-> Function won't receive both empty spaces with different lengths -> "   ", " " (don't mind this case)
-> what if we have punctuation or url or hastag or @ in the strings, consider them


C) General Steps to solve the problem (WHAT)
    
1. confirm if the input arguments are strings

2. create array of characters from the input strings, call them str1_list and str2_list
    
3. remove space and quotation("") from a and b
        
4. convert all characters to lower case
    
5. compare a and b. if all these conditions are met, they are anagrams.
if one of the conditions are not met, they are not anagrams
    
    a) check if their length is same
    b) if all characters in str1_list exist in str2_list
    c) if all characters in str2_list exist in str1_list
    


D) Pseudocode (HOW)

    1. Check type of the input arguments, if one is not a string, retrun False, else continue
    2. Convert input strings to the arrays of characters, e.g. ['a', 'b', 'c'], "list" built-in function is used
    3. Remove quotation and empty strings from the list of characters, Convert all characters to lower case, list comprehension is used
    4. Check if the two lists having the same length otherwise return false
    5. If they are having the same length
        a) check if all the characters in first list exist in second list, if not retrun false
        b) check if all the characters in second list exist in first list, if not return false
        c) if both a and b did not retrun False, then retrun True -> input strings are anagrams

"""
import time

def anagramsOrNot(str1, str2):
    
    ## the statement will execute when the if statement is True
    if (not isinstance(str1, str) or (not isinstance(str2, str))):
        return False
    ## save input strings as array of characters (list of str)
    str1_list = list(str1)
    str2_list = list(str2)
    ## clean list of characters from any number of empty space and change to lower case
    str1_list = [x.lower() for x in str1_list if not x == ' ']
    str2_list = [x.lower() for x in str2_list if not x == ' ']
    ## if their length are different, they are not anagrams
    if len(str1_list) == len(str2_list):
        ## if their length is same, but there is a character in first one
        ## that does not exist in second one -> not anagram
        for x in str1_list:
            if x not in str2_list:
                return False
        ## if their length is same, but there is a character in second one
        ## that does not exist in first one -> not anagram 
        for x in str2_list:
            if x not in str1_list:
                return False
        ## otherwise, both lists have the same number and type of characters -> anagram
        return True
    else:
        return False
       
        
start_time = time.time()
str1 = 'momm.'
str2 = '. omm/'  
a = anagramsOrNot(str1, str2)
print(a)
print("Time spent in seconds: ", time.time() - start_time)
    
    
    
    
    
    
    
    
    
    
    
  
  
