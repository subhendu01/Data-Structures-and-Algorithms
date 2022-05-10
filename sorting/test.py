def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        # divide into 2 lists
        left_list, right_list = list1[:mid], list1[mid:]
        merge_sort(left_list)
        merge_sort(right_list)

        # merge all the lists
        i, j, k = 0, 0, 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i += 1
                k += 1
            else:
                list1[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
            list1[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1

# num = int(input("Enter all the numbers:  "))
#
# list1 = [int(input()) for i in range(num)]

list1 = [34, 12, 10, 45, 0, 90, 11]
merge_sort(list1)
print(list1)

