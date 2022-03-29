def duplicate_value1(lst):
    dict = {}
    for i in lst:
        dict[i] = lst.count(i)
    return dict

def duplicate_value(lst):
    dict = {}
    for i in set(lst):
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


if __name__ == "__main__":
    lst = [2, 2, 3, 3, 4, 5, 6, 1, 3, 7]
    print(duplicate_value(lst))
