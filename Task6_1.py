from random import randint

"""
    Task 1

    The greatest number

    Write a Python program to get the largest number from a list of random 
    numbers with the length of 10

    Constraints: use only while loop and random module to generate numbers
"""

a = 0
num_list = []
while a <= 10:
    num_list = [randint(0, 999) for i in range(10)]
    print(num_list)
    b = max(num_list)
    print(f"Max integer in tuple: {b}\n")
    a += 1
