"""
Algorithm:
1. Find out the minimum value
2. Swap minimum value to 0th position
3. Take sublist(except sorted part) and repeat step 1 and step 2
"""


class SortArray:
    def __init__(self, arr):
        self.arr = arr

    def sort_array(self):
        for i in range(len(arr) - 1):
            arr_min = min(arr[i:])  # ASC
            # arr_max = max(arr[i:])  # DESC
            min_index = arr.index(arr_min, i)
            if arr[i] != arr[min_index]:
                arr[i], arr[min_index] = arr[min_index], arr[i]
            print(arr)
        return arr

    def sort_array_without_fun(self):
        for i in range(len(arr)-1):
            minimum = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j
            arr[i], arr[minimum] = arr[minimum], arr[i]
        return arr


arr = [34, 5, 6, 81, 0, 5]
obj = SortArray(arr)
print(obj.sort_array_without_fun())
