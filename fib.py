"""
Author: Justin Merwin
Program: fib.py

Purpose:
Recursively find n terms in the Fibonacci sequence.
I know this has been done many times, but this is my take on it.
"""

cache = {0: 0, 1: 1}

def fib(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]

while True:
    terms = []
    num_terms = int(input("How many terms deep would you like displayed? \n >>> "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
        continue
    else:
        for i in range(num_terms):
            terms.append(fib(i))
        print(*terms, sep=' - ')
        continue
