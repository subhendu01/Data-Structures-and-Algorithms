""""
Max Submatrix
Ninja has been given a matrix ‘MAT’ of integers having size ‘N’ x ‘M’ i.e. N rows and M columns. Ninja has to find the maximum sum submatrix in it. In other words, he has to find the maximum sum over all submatrices in the matrix.
For example: For the ‘MAT’ given below, the maximum sum submatrix having a sum of 29 is highlighted in red.

*** Input Format :
The first line of input contains an integer ‘T’ denoting the number of test cases. Then each test case follows.

The first line of each test case contains two space-separated integers ‘N’ and ‘M’ representing the number of rows and columns respectively. size of the matrix ‘MAT’.

The next ‘N’ lines of each test case contain ‘M’ single space-separated integers denoting the values of ‘MAT’.

*** Output Format :
For each test case, print the maximum sum over all submatrices in ‘MAT’.

Print the output of each test case in a separate line.

** Constraints :
1 <= ‘T’ <= 100
1 <= ‘N’, ‘M’<= 100
-100000 <= ‘MAT[i][j]’ <=100000

Where 'MAT[i][j]' represents the value at cell(i, j).

Time limit: 1 sec



*************************************************  Solution - 1 ********************************************************
Brute Force
The brute force approach is we check for every possible submatrix in the given ‘MAT’.

4 nested loops are required to select every submatrix of the matrix.
2 nested loops are required to take the sum of all the elements of the submatrix.
Here is the algorithm :

We declare a variable ‘MAX_SUM’ in which we store the maximum sum over all submatrices in the matrix.
We run a loop for ‘i’ = 0 to ‘N’:
We run a loop for ‘j’ = 0 to ‘M’:
We run a loop for ‘k’ = ‘i’ to ‘N’:
We run a loop for ‘l’ = ‘j’ to ‘M’:
We declare a variable ‘tmpSum’ in which we store the sum of the current submatrix
We run a loop for ‘q’ = ‘i’ to ‘k’:
We run a loop for ‘r’ = ‘j’ to ‘l’:
‘tmpSum’ += mat[q][r]
‘maxSum’ = max(‘maxSum’, ‘tmpSum’)
Finally, we return ‘MAX_SUM’.
Space Complexity: O(1)Explanation:
O(1).



Because we are not using any extra space for finding our resultant answer.

Time Complexity: OtherExplanation:
O((N * M) ^ 3) Where ‘N’ and ‘M’ denote the number of rows and columns of the matrix ‘MAT’.



Because we are using 6 nested loops. 4 nested loops are required to select every submatrix of the matrix And 2 nested
loops are required to take the sum of all the elements of the submatrix. Hence, the overall time complexity
is O((N * M) ^ 3).

*************************************************  Solution - 2 ********************************************************
Kadane's Algorithm
As we know, we have to find the maximum sum submatrix. So, the idea is; first, we fix the left and right columns of the ‘MAT’. Then try to find the sum of elements of the submatrix from the left column to the right column for each row and store these values in a ‘MAX_SUM_VALUES’ array/list. After this, we apply Kadane’s algorithm on this array/list ‘MAX_SUM_VALUES’.



Here is the algorithm :

We declare a variable ‘MAX_SUM’ in which we store the maximum sum over all submatrices in the matrix.
We run a loop for ‘i’ = 0 to ‘M’:
We declare an array/list ‘MAX_SUM_VALUES’ in which we store the sum of elements of the submatrix from the left column to the right column for each row
We run a loop for ‘j’ = ‘i’ to ‘M’:
We run a loop for ‘k’ = 0 to ‘N’:
‘MAX_SUM_VALUES[k]’ += ‘MAT[k][j]’
Apply kadane’s algorithm on this array/vector ‘MAX_SUM_VALUES’ and if the output is greater than ‘MAX_SUM’ then we update the value of ‘MAX_SUM’.
Finally, we return ‘MAX_SUM’.
Kadane’s algorithm:

We declare two variables ‘MAX_SO_FAR’ and ‘MAX_ENDING_HERE’ in which we store the maximum sum of contiguous subarray and maximum sum of contiguous subarray if we include the current element.
Initialize ‘MAX_SO_FAR’ and ‘MAX_ENDING_HERE’ with ‘MAX_SUM_VALUES[0].
We run a loop for ‘i’ = 1 to ‘N’:
‘MAX_ENDING_HERE’ = max(‘MAX_ENDING_HERE’ + ‘MAX_SUM_VALUES[i]’ , ‘MAX_SUM_VALUES[i]’)
 ‘MAX_SO_FAR’ = max(‘MAX_SO_FAR’, ‘MAX_ENDING_HERE’)
Finally, return ‘MAX_SO_FAR’.
Space Complexity: O(n)Explanation:
O(N)  Where ‘N’ denotes the number of rows of the matrix ‘MAT’.



Because we are using a ‘MAX_SUM_VALUES’ array/list of size ‘N’.

Time Complexity: O(n^3)Explanation:
O((M ^ 2) * N) Where ‘N’ and ‘M’ denote the number of rows and columns of the matrix ‘MAT’.



Because we are using three nested loops. The first loop is used to traverse all the columns of ‘MAT’, the second loop is
used to traverse the rows of the selected columns and the third loop is used to find the maximum sub-array sum in
‘MAX_SUM_VALUES’ array/list using Kadane’s algorithm. Hence, the overall time complexity is O((M ^ 2) * N).
"""

# Solution

"""
Time complexity: O((M ^ 2) * N)
Space complexity: O(N) 
Where N, M is the number of rows and columns of the matrix MAT.
"""


# This function will return largest subarray sum using Kadane's algo
def Kadane(maxSumValue):
    maxSoFar = maxSumValue[0]
    maxEndingHere = maxSumValue[0]
    for i in range(1, len(maxSumValue)):
        # Update value of subarray sum ending at index 'i' and max subarray sum till now
        maxEndingHere = max(maxEndingHere + maxSumValue[i], maxSumValue[i])
        maxSoFar = max(maxSoFar, maxEndingHere)
    # Return largest sum
    return maxSoFar


def maxSumSubmatrix(mat, n, m):
    # Initialize 'maxSum'
    maxSum = -(2 ** 31)
    for i in range(m):
        # Array that will store sum of values from column 'i' to  column 'j'
        maxSumValues = [0] * n
        for j in range(i, m):
            # Add values of current row
            for k in range(n):
                maxSumValues[k] += mat[k][j]
            # Using kadane's algorithm find maxSum
            maxSum = max(Kadane(maxSumValues), maxSum)
    # Return maxSum achieved
    return maxSum
