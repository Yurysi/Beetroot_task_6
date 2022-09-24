"""
    Task 3

    Extracting numbers.

    Make a list that contains all integers from 1 to 100, then find
    all integers from the list that are divisible by 7 but not a multiple
    of 5, and store them in a separate list. Finally, print the list.

    Constraint: use only while loop for iteration
"""
first_list = list(range(1, 100 + 1))
second_list = []
print(first_list, '\n')

a = 0
s = 0
while a < 100 or a == 99:
    if first_list[a] % 7 == 0:
        second_list.append(first_list[a])

        a += 1
    else:
        a += 1

while s < len(second_list):
    if second_list[s] % 5 == 0:
        del second_list[s]
        s += 1
    else:
        s += 1
print(f"This is completed list:\n{second_list}")
