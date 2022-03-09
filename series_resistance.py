"""
Program: series_resistance.py
Author: Justin Merwin (jmerwin@grantham.edu)
Purpose: This is my solution to the following challenge:
https://edabit.com/challenge/gzmFeaXwFv8X6pBGq

I'm only sharing it because I think it's a pretty nifty
for loop example.
"""

def series_resistance(first):
    i = 0
    RT = 0
    for i in len(first):
        RT = RT + first[i]
        i += 1
    if RT <= 1:
        return str(RT) + " ohm"
    else:
        return str(RT) + " ohms"
