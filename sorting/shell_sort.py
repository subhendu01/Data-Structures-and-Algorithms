"""
ShellSort is a variation of insertion sort.
Sometimes called as "diminishing increment sort".

How ShelSort improves insertion sort algorithm?
    By breaking the original list into a number of sub-lists, each sublist is sorted using the insertion sort.
    It will move the items nearer to its original index.

Algorithms:
    1. Take the list of numbers
    2. Find out the gap/incrementor
    3. Create the sub-list based on gap and sort them using insertion sort algorithm
    4. Reduce gap and repeat step 3.
    5. Stop when gap is 0.

"""


def shell_sort(list1):
    gap = len(list1) // 2

    while gap > 0:
        for index in range(gap, len(index)):
            current_element = list1[index]
            pos = index

            while pos >= gap and current_element < list1[pos - gap]:
                list1[pos] = list1[pos - gap]
                pos = pos - gap

            list1[pos] = current_element

        gap = gap // 2
