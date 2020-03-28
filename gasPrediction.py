#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:49:38 2020

@author: marjan

Question:
    Uber is introducing a new feature for drivers that tells them if they'll need gas within the next hour.
    It analyzes all of the drive distances (in miles) that the driver has traveled in the past 12 hours to
    make the recommendation. Given the current gas level (in gallons), the drive data, and the average mileage
    of the vehicle, calculate the average amount of gas spent per hour and return true if the driver is likely
    to need a refill in the next hour, false otherwise.
    Assume that the driver will need more gas if the average gas consumption per hour is greater than
    the amount of gas they have at the given moment. The average mileage is measured in miles per gallon
    and it shows how many miles a vehicle can travel on one gallon of gas.
    
Redefine the question:
    a) an array of float numbers is given that determines the milages that the vehicle went through in the past 12 hours
    b) a float is given which determines current gas level in the vehicle 
    c) a float is given which determines how many miles the vehicle can travel on one gallon of gas
    d) calculate the average gas spent in one hour and compare it with current gas level
    e) if average gas per hour is larger than the current gas level, return True (driver need gas within the next hour)
    f) if average gas per hour is less than the current gas level, return False (driver does not need gas within the next hour)
    
    
Consider all possible cases:
    a) input types are array of floats (distance in mile), int (number of hours), float (gas in gallon), float (average miles per one gallon gas)
    b) what if current gas level is equal to the gas consumtion per hour --> retrun True
    
    
Steps to solve the problem:
    a) Find sum of the elements in driveDistances
    b) Consider the distance travelled in numberOfHours to calculate (proportional problem) miles traveled per hour 
    c) Consider miles traveled on one gallon to calculate (proportional problem) gas needed for [miles traveled per hour] == gas needed per hour
    d) Compare current gas level with gas needed per hour, if larger return False, if less than or equal return True

"""

def gasPrediction(driveDistances, numberOfHours, currentGasLevel, avgMileage):
    """
    in: array of float, int, float, float
    out: boolean (true or false)
    """
    
    total_distance = sum(driveDistances)
    miles_per_hour = total_distance / numberOfHours
    gallon_per_hour = miles_per_hour / avgMileage
    
    if currentGasLevel > gallon_per_hour:
        return False
    else:
        return True
    
driveDistances = [12, 6, 17, 5, 20]
numberOfHours = 12
currentGasLevel = 0.25
avgMileage = 25.0
print(gasPrediction(driveDistances, numberOfHours, currentGasLevel, avgMileage))
    
    
    
    
    
    
    