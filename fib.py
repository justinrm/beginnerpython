"""
Author: Justin Merwin
Program: fib.py

Purpose:
Recursively find n terms in the Fibonacci sequence.
I know this has been done many times, but this is my take on it.
"""

from functool import cache

@cache
def fib(n):
    if n in {0, 1}:
        return n
    else:
        return fib(n-1) + fib(n-2)

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
