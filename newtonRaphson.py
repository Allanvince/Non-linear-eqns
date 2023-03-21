# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 02:12:03 2023

@author: user
"""
#Newton Raphson
from timeit import Timer

def newton_raphson():
    def f(x):
        return x**3 -2*x -6

    def df(x):
        return 3*x**2 - 2

    y = 1
    tolerance = 1e-6
    maxIterations = 100

    for i in range(maxIterations):
        fx = f(y)
        dfx = df(y)
        x1 = y - fx/dfx
        
        print(f"Iterations = {i}")
        if abs(f(x1)) < tolerance:
            print(f"Root found at x = {x1:.6f}")
            break
        else:
            y = x1
        
t = Timer("newton_raphson()", "from __main__ import newton_raphson")
print("Time taken: " +str(t.timeit(1))+ "seconds.")