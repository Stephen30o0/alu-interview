#!/usr/bin/python3
"""Calculates the minimum number of Copy and Paste
operations needed to get n H characters in a text file
"""


def minOperations(n):
    """return 0 if n is impossible to achieve"""
    if n <= 0:
        return 0
    
    operations = 0
    i = 2 # 
    
    """divide n by i as many times as possible"""
    while i <= n:
        while n % i == 0:
            operations += i 
            n = n // i 
        i += 1 
    
    """if n is still greater than 1, add n as the final operation"""
    if n > 1:
        operations += n
    
    return operations 
