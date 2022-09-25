from random import randint

"""
    Task 2

    Exclusive common numbers.

    Generate 2 lists with the length of 10 with random integers from 1 to 10,
     and make a third list containing the common integers between the 2
     initial lists without any duplicates.

    Constraints: use only while loop and random module to generate numbers
"""
first_list = [randint(1, 10) for item in range(10)]
second_list = [randint(1, 10) for item in range(10)]
third_list = []
a = 0
print(f"first_list: {sorted(first_list)}\nsecond_list: {sorted(second_list)}\n")
while a < 10:
    if first_list[a] in second_list:
        third_list.append(first_list[a])
        a += 1
    else:
        a += 1
third_list = list(set(third_list))
print(f"This is list without dublicates:\n{sorted(third_list)}")
