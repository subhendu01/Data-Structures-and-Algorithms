def reverse_iterative(lst):
    l = len(lst)
    for i in range(int(l/2)):
        # Swap each number with the number in
        # the mirror position for example first
        # and last
        n = lst[i]
        lst[i] = lst[l-i-1]
        lst[l-i-1] = n
    return lst

def reverse_recursive_sol(lst):
    if len(lst) == 1:
        return lst
    return reverse_recursive_sol(lst[1:]) + lst[0:1]

def reverse_(lst):
    return lst[::-1]

def _reverse_(lst):
    return [i for i in reversed(lst)]

def reverse_1(lst):
    lst.reverse()
    return lst

if __name__ == "__main__":
    lst = [10, 19, 1, 27, 9]
    print(reverse_recursive_sol(lst))

