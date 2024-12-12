"""
Program: series_resistance.py
Author: Justin Merwin
Purpose: Solve the series resistance challenge:
https://edabit.com/challenge/gzmFeaXwFv8X6pBGq

This solution demonstrates the use of Python's built-in
functions for a concise and efficient implementation.
"""

def series_resistance(resistances):
    """
    Calculate the total resistance of resistors in series.
    
    Args:
        resistances (list of float): A list of resistance values in ohms.
    
    Returns:
        str: Total resistance as a string, formatted with "ohm" or "ohms".
    """
    total_resistance = sum(resistances)
    unit = "ohm" if total_resistance <= 1 else "ohms"
    return f"{total_resistance} {unit}"
