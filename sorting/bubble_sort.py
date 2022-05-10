"""Some times referred as sinking sort, is a simple sorting algorithm which sorts n number of elements in the list by
comparing the each pair of adjucent items and swaps them if they are in wrong order.

Algorithm: (Ascending order)
1. Staring with the first element (index=0) compare the current element with the next element of the list.

2. If the current element is greater than the next element of the list swap them.

3. If the current element is less than the next element, move to the next element. Repeat step 1.

Ex:
10  15  4   23  0

first - iteration:
first swap - 10  15  4  23  0
second swap- 10  4  15  23  0
             10  4  15  23  0
             10  4  15  0   23

second - iteration:
             4 10 15 0 23
             4 10 15 0 23
             4 10 0 15 23

third - iteration:
             4 10 0 15 23
             4 10 0 15 23
             4 0 10 15 23
.
.
.
"""
lst = [10, 15, 4, 23, 0]
for j in range(len(lst) - 1):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)

# ----- OR -----

lst = [10, 15, 4, 23, 0]
for j in range(len(lst) - 1):
    for i in range(len(lst) - 1 - j):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)

# ------ OR -------
lst = [10, 15, 4, 23, 0]
for j in range(len(lst) - 1, 0, -1):
    for i in range(j):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)

