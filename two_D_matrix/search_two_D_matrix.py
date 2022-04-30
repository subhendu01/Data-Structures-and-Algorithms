"""
74.
Write a effective algorithm that search for a target value in an m x n matrix. the matrix has the following properties.
    1. Integers in each row are sorted in ascending from left to right.
    2. Integers in each column are sorted in ascending from top to bottom.

Example 1:
            1   4   7    11     15

            2   5   8    12     19

            3   6   9    16     22

            10  13  14   17     24

            18  21  23   26     30

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24][18,21,23,26,30]], target = 12
Output: true

"""

# we can do a binary search in every single rows (complexity n x m), it'll not give surety that columns are sorted
# both in col and row binary search will not work.

# binary search complexity ===>>> logn (for 1D)
# binary search complexity ===>>> mlogn (for 2D)

# Here we will use binary search for only that particular row search ===>> logm + logn

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N, M = len(matrix), len(matrix[0])  # find the length
        r, c = N - 1, 0   # row, col value for staring point

        while r >= 0 and c < M:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                r -= 1  # move-up the row
            else:
                c += 1  # shift right the col
        return False

