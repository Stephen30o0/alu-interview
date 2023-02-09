#!/usr/bin/python

def minOperations(n):
    if n == 0:
        return 0
    operations = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            operations += i
            n = n // i
        i += 1
    if n > 1:
        operations += n
    return operations
