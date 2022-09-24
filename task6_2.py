from random import randint

"""
    Task 2

    Exclusive common numbers.

    Generate 2 lists with the length of 10 with random integers from 1 to 10,
     and make a third list containing the common integers between the 2
     initial lists without any duplicates.

    Constraints: use only while loop and random module to generate numbers
"""
first_list = []
second_list = []
third_list = []
a = 0
while a < 1:
    first_list = [randint(1, 10) for item in range(10)]
    second_list = [randint(1, 10) for item in range(10)]
    a += 1
    third_list.extend(first_list)
    third_list.extend(second_list)
    third_list = list(set(third_list))
    print(f"first_list: {first_list}\nsecond_list: {second_list}\n")
    print(f"This is list without dublicates:\n{third_list}")
