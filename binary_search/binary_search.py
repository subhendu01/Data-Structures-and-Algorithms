def linear_search(lst, num_to_find):
    for i in lst:
        if i == num_to_find:
            return True
    return False

def binary_search(lst, num_to_find):
    left_index = 0
    right_index = len(lst) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_num = lst[mid_index]

        if mid_num == num_to_find:
            return mid_index

        if mid_num < num_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1

def binary_search_recursion(ltr, num_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_numb = ltr[mid_index]

    if mid_numb == num_to_find:
        return mid_index

    if mid_numb < num_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursion(ltr, num_to_find, left_index, right_index)

def find_occurance(lst, num):
    count = 0
    for i in lst:
        if i == num:
            count += 1
    return count

if __name__ == "__main__":
    lst = [12, 15, 18, 29, 45, 45, 79]
    print(binary_search(lst, 15))
    # print(binary_search_recursion(lst, 29, 0, len(lst)))
    # print(find_occurance(lst, 79))