"""
Author: Justin Merwin
Program: fib.py

Purpose:
Recursively find n terms in the Fibonacci sequence. This implementation
demonstrates input validation, recursive logic with caching, and clean output.
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Recursively calculate the nth Fibonacci number with caching.
    
    Args:
        n (int): The position in the Fibonacci sequence.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def get_fibonacci_sequence(num_terms):
    """
    Generate the Fibonacci sequence up to num_terms.
    
    Args:
        num_terms (int): The number of terms in the sequence.
        
    Returns:
        list of int: Fibonacci sequence up to the specified number of terms.
    """
    return [fibonacci(i) for i in range(num_terms)]

def main():
    """
    Main function to handle user input and display the Fibonacci sequence.
    """
    while True:
        try:
            num_terms = int(input("How many terms deep would you like displayed? (Enter 0 to exit)\n>>> "))
            if num_terms == 0:
                print("Exiting the program. Goodbye!")
                break
            if num_terms < 0:
                print("Please enter a positive integer.")
                continue
            sequence = get_fibonacci_sequence(num_terms)
            print(" - ".join(map(str, sequence)))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
