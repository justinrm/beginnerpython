# Author: Justin Merwin
# Program: fib.py
#
# Purpose:
#
# Recursively find n terms in the Fibonacci sequence.
# I know this has been done many times, but this is my take on it.
#
# ISSUES:
#   - Currently, larger numbers (around 50) make the program freeze up on computers with less power.
#     I don't know how to make it work any better. Perhaps using a cache of sorts?

def fib(n):
    if n <= 1:
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
