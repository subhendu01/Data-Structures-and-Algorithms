"""
Algorithm:
Also called as Partition Exchange sort.
Developed by Tony Hoare in 1959 and published in 1961
When implemented well it can be about 2 or 3 times faster than the its main competitor merge sort and heap sort.

Quick Sort:
1. Comparison Sort
2. In_place sort (it may required more memory)
3. Unstable sort
4. Recursive Algorithm

Divide and Conquer Algorithm:
1. Divide
2. Conquer
3. Combine

For ascending order:
    <Smaller Value> <Pivot> <Bigger value>
For descending order:
    <Bigger Value> <Pivot> <Smaller Value>

Pivot Element:
1. First element    (In case of sorted list we should avoid this because if we consider this then left/right side there won't be any value(s).)
2. Last element
3. Random element
4. Median of three values (first, middle, last)

1. left <= right
2. a[left] <= pivot
3. a[right] >= pivot

Algorithm to solve :
1. Select the pivot element
2. Find out the correct position of the pivot element in the list by rearranging it.
3. Divide the list based on pivot element.
4. Sort the sublist recursively.

Solution flow:
We will use 3 functions
1. To find the pivot
2. Divide the list to sublist and here we'll use recursive method
3. Main method to take i/p

index  0        1     2     3     4     5
list   56       26    93    17    31    44
     (pivot)   (left)                 (right)
"""

# taking first element as pivot

def pivot_pos_first(list1, first, last):
    pivot = list1[first]
    left = first + 1
    right = last
    while True:
        while left <= right and list1[left] <= pivot:  # for descending list1[left] >= pivot
            left += 1
        while left <= right and list1[right] >= pivot:  # for descending list1[right] >= pivot
            right -= 1

        if right < left:
            # list1[first], list1[right] = list1[right], list1[first]
            break
        else:  # when list1[left] <= pivot and list1[right] >= pivot got false
            list1[left], list1[right] = list1[right], list1[left]
    list1[first], list1[right] = list1[right], list1[first]

    return right


def quick_sort_first(list1, first, last):
    if first < last:
        p = pivot_pos_first(list1, first, last)
        quick_sort_first(list1, first, p-1)  # divide the list (left)
        quick_sort_first(list1, p+1, last)    # divide the list (right)


if __name__ == "__main__":
    list1 = [56, 26, 93, 17, 31, 44]
    quick_sort_first(list1, 0,  len(list1) - 1)
    print(list1)




# taking last element as pivot
def pivot_pos_last(list1, first, last):
    pivot = list1[last]
    left = first
    right = last - 1
    while True:
        while left <= right and list1[left] <= pivot:  # for descending list1[left] >= pivot
            left += 1
        while left <= right and list1[right] >= pivot:  # for descending list1[right] >= pivot
            right -= 1

        if right < left:
            # list1[first], list1[right] = list1[right], list1[first]
            break
        else:  # when list1[left] <= pivot and list1[right] >= pivot got false
            list1[left], list1[right] = list1[right], list1[left]
    list1[last], list1[left] = list1[left], list1[last]

    return left


def quick_sort_last(list1, first, last):
    if first < last:
        p = pivot_pos_last(list1, first, last)
        quick_sort_last(list1, first, p-1)  # divide the list (left)
        quick_sort_last(list1, p+1, last)    # divide the list (right)


if __name__ == "__main__":
    list1 = [56, 26, 93, 17, 31, 44]
    quick_sort_last(list1, 0,  len(list1) - 1)
    print(list1)



# taking random element as pivot
import random
def pivot_pos_random(list1, first, last):
    rindex = random.randint(first, last)
    list1[rindex], list1[last] = list1[last], list1[rindex]
    pivot = list1[last]
    left = first
    right = last - 1
    while True:
        while left <= right and list1[left] <= pivot:  # for descending list1[left] >= pivot
            left += 1
        while left <= right and list1[right] >= pivot:  # for descending list1[right] >= pivot
            right -= 1

        if right < left:
            # list1[first], list1[right] = list1[right], list1[first]
            break
        else:  # when list1[left] <= pivot and list1[right] >= pivot got false
            list1[left], list1[right] = list1[right], list1[left]
    list1[last], list1[left] = list1[left], list1[last]

    return left


def quick_sort_random(list1, first, last):
    if first < last:
        p = pivot_pos_random(list1, first, last)
        quick_sort_random(list1, first, p-1)  # divide the list (left)
        quick_sort_random(list1, p+1, last)    # divide the list (right)


if __name__ == "__main__":
    list1 = [0, 56, 26, 93, 17, 31, 31, 44, 0]
    quick_sort_random(list1, 0,  len(list1) - 1)
    print(list1)


# taking median element as pivot

import statistics


def pivot_pos_median(list1, first, last):

    low = list1[first]
    high = list1[last]
    middle = (first+last)//2
    pivot_value = statistics.median([low, list1[middle], high])

    if pivot_value == low:
        pindex = first
    elif pivot_value == high:
        pindex = last
    else:
        pindex = middle

    list1[pindex], list1[last] = list1[last], list1[pindex]

    pivot = list1[last]
    left = first
    right = last - 1
    while True:
        while left <= right and list1[left] <= pivot:  # for descending list1[left] >= pivot
            left += 1
        while left <= right and list1[right] >= pivot:  # for descending list1[right] >= pivot
            right -= 1

        if right < left:
            # list1[first], list1[right] = list1[right], list1[first]
            break
        else:  # when list1[left] <= pivot and list1[right] >= pivot got false
            list1[left], list1[right] = list1[right], list1[left]
    list1[last], list1[left] = list1[left], list1[last]

    return left


def quick_sort_median(list1, first, last):
    if first < last:
        p = pivot_pos_median(list1, first, last)
        quick_sort_median(list1, first, p-1)  # divide the list (left)
        quick_sort_median(list1, p+1, last)    # divide the list (right)


if __name__ == "__main__":
    list1 = [0, 56, 26, 93, 17, 31, 31, 44, 0]
    quick_sort_median(list1, 0,  len(list1) - 1)
    print(list1)