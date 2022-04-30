
'''
Shopping Options You are given the list of costs of pants in an array “pants”,
shirts in an array “shirts”, shoes in an array “shoes”, and skirts in an array “skirts”.
You are also given a budget amount ‘X’ to spend. You want to buy exactly 1 item from each list.
Your task is to determine the total number of possible combinations that you can buy, given that the total
amount of your purchase does not exceed your budget amount.

*** Input Format ***:
The first line of input contains an integer ‘T’ denoting the number of test cases to run. Then the test case follows.

The first line of each test case contains five integers ‘P’, ‘Q’, ‘R’, ‘S’ and, ‘X’. Denotes the number of pants, shirts, shoes, skirts, and budget amount respectively.

The second line of each test case contains exactly ‘P’ integers. Denotes the cost of each pant.

The third line of each test case contains exactly ‘Q’ integers. Denotes the cost of each shirt.

The fourth line of each test case contains exactly ‘R’ integers. Denotes the cost of each shoe.

The fifth line of each test case contains exactly ‘S’ integers. Denotes the cost of each skirt.

*** Output Format ***:
For each test case, return an integer that represents the total number of combinations to buy that are valid according to the above conditions.

Output for each test case will be printed in a new line.

*** Constraints:
1 <= T <= 100
1 <= ‘P’, ‘Q’, ‘R’, ‘S’  <= 10
1 <= ‘X’ <= 10^9
1 <= pants[i], shirts[i], shoes[i], skirts[i] <= 10^9

Time Limit: 1 sec


******************************************************  Solution ****************************************************************
Brute Force
We can check all possible combinations to buy items. That can be done by maintaining a variable “answer” and iterating over all four lists in a nested way such that each pant, shirt, shoe, and skirt pair can get selected and find the sum of that pair. If sum is less than or equal to budget then increment “answer” by one. Return the “answer”.


Algorithm:

Create an integer “answer” equal to 0.
First iterate over the list of pants, for each pant:
Then, iterate over the list of shirts, for each shirt:
Then, iterate over the list of shoes, for each shoe:
Then, iterate over the list of skirts, for each skirt:
If the sum of cost of pant, shirt, shoe, and skirt is less than or equal the amount of budget, then increment the answer by one.
Else do nothing.
Return “answer”.
Space Complexity: O(1)Explanation:
O(1)



Constant extra space is required. Hence, the overall Space Complexity is O(1).

Time Complexity: O(1)Explanation:
O(P * Q * R * S), where ‘P’, ‘Q’, ‘R’, and ‘S’ denote the number of pants, shirts, shoes, skirts respectively.



Since we are checking all possible combinations iterating over all four lists in a nested way. Therefore time complexity is O(P * Q * R * S).

'''


'''
    Time Complexity: O(P * Q * R * S)
    Space Complexity: O(1)
    Where P, Q, R, and S denote the number of pants, shirts, shoes, skirts respectively.
'''
def shoppingOptions(pants, shirts, shoes, skirts, budget):
    # To store number of ways to buy
    answer = 0
# To generate every possible combinations
    for i in range(len(pants)):
        for j in range(len(shirts)):
            for k in range(len(shoes)):
                for l in range(len(skirts)):
                    if (pants[i] + shirts[j] + shoes[k] + skirts[l] <= budget):
                        answer = answer + 1
    # Rerturn answer.
    return answer
