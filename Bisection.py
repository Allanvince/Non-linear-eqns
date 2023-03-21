# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 06:45:30 2023

@author: user
"""

# Bisection method
import math

from timeit import Timer
def bisection():
    def f(x):
        return x**3 - 2*x - 6


    a = 2
    b = 3
    tolerance = 1e-6
    maxIterations = 50

    for i in range(maxIterations):
        c = (a+b)/2
        print(f"Iteration number: {i}")
        if abs(f(c) < tolerance):
            print(f"Roots found at x = {c:.6f}")
            break
        elif f(c) * f(a) < 0:
            maxIterations = 50
            b = c
        else:
            a = c

t = Timer("bisection()", "from __main__ import bisection")
print("Time taken: " +str(t.timeit(1))+ "seconds.")