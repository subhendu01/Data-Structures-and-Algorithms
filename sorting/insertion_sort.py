"""
It is a simple sorted algorithm, that builds the final sorted list one item at a time

** it's like soring the cards

Algorithm:
    1. Consider the first element to be sorted and the rest to be unsorted.
    2. Take the first element in the unsorted part(u1) and compare it with sorted part elements(s1).
    3. If u1<s1 then insert u1 in the correct index, else leave it as it.
    4. Take next elements in the unsorted part and compare with sorted elements.
    5. Repeat 3 and 4 until all the elements are sorted.
"""


def insertion_sort(list1):
    for index in range(1, len(list1)):
        current_element = list1[index]
        pos = index

        while current_element < list1[pos - 1] and pos > 0:
            list1[pos] = list1[pos - 1]
            pos -= 1
        list1[pos] = current_element


list1 = [9, 35, 0, 15, 11]
insertion_sort(list1)
print(list1)

