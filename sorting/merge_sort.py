"""
Merge Sort:
    1. Divide and conquer algorithm (divide big list into 2 sub-list)
            a. Divide
            b. Conquer
            3. Combine

Algorithm:
    1. Split the unsorted list
    2. compare each of the element and group them
    3. repeat step-2 until whole list is merged and sorted

"""

def merger_sort(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        left_list, right_list = list1[:mid], list1[mid:]
        # print(left_list, right_list)
        merger_sort(left_list)
        merger_sort(right_list)

        i, j, k = 0, 0, 0  # i is for left list / j is for right list/ k is for original list
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:   # for decending left_list[i] > right_list[j]
                list1[k] = left_list[i]
                i += 1
                k += 1
            else:
                list1[k] = right_list[j]
                j += 1
                k += 1

        # added the left over values
        while i < len(left_list):
            list1[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1


# num = int(input("Enter the number of elements:  "))
# list1 = [int(input()) for i in range(num)]
list1 = [1,2,3,4,5,6,0,9]
print(list1)
merger_sort(list1)

print(f"sorted list {list1}")
