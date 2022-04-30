"""
Add Linked Lists
Given two numbers represented by linked lists. Your task is find the sum list and return the head of the sum list.
The sum list is a linked list representation of addition of two numbers.

*** Input Format :
The first line of input contains a single integer T, representing the number of test cases or queries to be run.

Then the T test cases follow.

The first line of each test case contains the elements of the first singly linked list separated by a single space and
terminated by -1. Hence, -1 would never be a list element.

The second line of each test case contains the elements of the second singly linked list separated by a single space and
terminated by -1. Hence, -1 would never be a list element.

*** Output Format :
For each test case, print the sum linked list. The elements of the sum list should be single-space separated, terminated by -1.

The output of each test case is printed in a separate line.

*** Constraints :
1 <= T <= 10
1 <= N <= 5 * 10^4
0 <= data <= 9 and data != -1


Time Limit : 1sec

*********************************************  Solution - 1 ************************************************************
Recursive approach
One way is to recursively add the two linked lists. Keep the nodes in the recursion stack and add the last nodes first and then second last and so on. Initially, find the size of both the linked lists. If both the linked lists are of the same size, add them using recursion. Else if their sizes differ, move the head pointer of the larger linked list forward K times, where K is the difference between the number of nodes in the larger linked list and the smaller one. Now calculate the sum of these two linked lists using recursion and add the carry of the resultant list and the left part of the larger linked list.

Algorithm :

Calculate sizes of given two linked lists.
If both the lists are of same size, then calculate their sum using recursion. Hold all nodes in the recursion call stack, till the rightmost node. Calculate sum of the rightmost nodes and forward carry to the left side. If at the end of addition, a non zero carry exists, insert it at the beginning of the sum list through a new Linked List node.
If the lists differ in size. Let the difference be ‘diff’.
a.  Move diff nodes ahead in the larger linked list. Now use step 2 to add the smaller list and the right sub-list of the larger list. Also store the carry of this sum.
b.  Add the carry and the left part of the larger linked list.
c.  Append the nodes of this sum list are at the beginning of the previous sum list calculated in 3a.
Return the head of the sum list.
Space Complexity: O(n)Explanation:
O(max(N,M)), where ‘N’ and ‘M’ are the number of nodes in the first and the second linked list respectively.



After moving the pointer on the larger list to the node from where its size is equal to the size of the smaller linked list, both the lists to be added are now of min(N,M) size. Both the lists use recursion stack to store the nodes until the rightmost node is reached. This results into a space complexity of O(2*(min(N,M))). Also, a new linked list is created for storing the sum of the two linked lists, which results in a space complexity of O(max(N,M)).

Final space complexity will be  O(min(N,M)) + O(max(N,M)) = O(max(N,M)).

Time Complexity: O(n)Explanation:
O(N+M), where ‘N’ and ‘M’ are the number of nodes in the first and the second linked list respectively.



Every node of the both the linked lists is visited twice to calculate the size of the lists and to perform the addition operation. So the time complexity is O(2*(N+M)) = O(N+M).

*********************************************  Solution - 2 ************************************************************
Iterative approach
The idea is to use the simple method of adding two numbers. We add two numbers starting from their least significant digit and moving towards the most significant digit. So we need to access the nodes of linked lists from last to first. First step would be to reverse both the linked lists. Then add both the linked lists starting from their heads and then reverse the resulting sum list and return its head.



Algorithm :

Reverse both the linked lists.
Add corresponding nodes of the two linked lists and take the carry forward, if any. If the value of carry after addition is non-zero, insert the carry at the end of the sum list through a new linked list node.
Reverse the added linked list and return its head.
Space Complexity: OtherExplanation:
O(max(N,M)), where ‘N’ and ‘M’ are the number of nodes in the linked lists first and second respectively.



New linked list is created for storing the sum of the two linked lists. Thus the space complexity will be O(max(N,M)).

Time Complexity: O(n)Explanation:
O(N + M), where ‘N’ and ‘M’ are the number of nodes in the linked lists first and second respectively.



Each element of the linked list is visited once. So, the time complexity will be O(N + M).

"""

# solutution -1
'''
    Time Complexity: O(N + M)
    Space Complexity: O(max(N,M))
    Where N and M are the number of nodes in the first and the second linked list respectively.
'''
# List Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __del__(self):
        if(self.next):
            del self.next
# Returns size of linked list
def getSize(head):
    size = 0
    while(head != None):
        size += 1
        head = head.next
    return size
def swapPointers(a, b):
    return b, a
def addSameSize(head1, head2, carry):
    # Since both the lists are of same size
    if(head1 == None):
        return carry, None
    sum = 0
    # Allocate memory for sum node of current two nodes
    result = Node(0)
    # Recursively add remaining nodes and get the carry
    carry, result.next = addSameSize(head1.next, head2.next, carry)
    # Add digits of current nodes and propagated carry
    sum = head1.data + head2.data + carry
    carry = sum // 10
    sum = sum % 10
    # Assign the sum to current node of resultant list
    result.data = sum
    return carry, result
# Pushes new node at the beginning of linked list
def push(head, carry):
    temp = Node(0)
    temp.data = carry
    temp.next = head
    head = temp
    return head
def addCarryToRemaining(head1, cur, carry, result):
    sum = 0
    # If diff number of nodes are not traversed, add carry
    if (head1 != cur):
        carry, result = addCarryToRemaining(head1.next, cur, carry, result)
        sum = head1.data + carry
        carry = sum // 10
        sum %= 10
        # Add this node to the front of the result
        result = push(result, sum)
    return carry, result
def addLL(head1, head2):
    cur, result = None, None
    # First list is empty
    if (head1 == None):
        result = head2
        return result
    # Second list is empty
    elif (head2 == None):
        result = head1
        return result
    # Removing leading zeros from first list
    while(head1 != None and head1.data == 0):
        head1 = head1.next
    # Removing leading zeros from second list
    while(head2 != None and head2.data == 0):
        head2 = head2.next
    size1 = getSize(head1)
    size2 = getSize(head2)
    carry = 0
    # Add same sized lists
    if (size1 == size2):
        carry, result = addSameSize(head1, head2, carry)
    else:
        diff = abs(size1 - size2)
        # First list should always be larger than second list. If not, swap pointers
        if (size1 < size2):
            head1, head2 = swapPointers(head1, head2)
        # move diff. number of nodes in first list
        cur = head1
        for i in range(diff):
            cur = cur.next
        # get addition of same size lists
        carry, result = addSameSize(cur, head2, carry)
        # get addition of remaining first list and carry
        carry, result = addCarryToRemaining(head1, cur, carry, result)
    # If some carry is still there, add a new node to the front of the result list
    if (carry != 0):
        result = push(result, carry)
    return result

# solution - 2
'''
    Time Complexity: O(N + M)
    Space Complexity: O(max(N,M))
    Where N and M are the number of nodes in the first and the second linked list respectively.
'''
# List Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __del__(self):
        if(self.next):
            del self.next
# Reverses the linked list
def reverse(head):
    prev = None
    curr = head
    while(curr != None):
        ahead = curr.next
        curr.next = prev
        prev = curr
        curr = ahead
    return prev
def addLL(head1, head2):
    # If first linked list is empty return second
    if(head1 == None):
        return head2
    # If second linked list is empty return first
    if(head2 == None):
        return head1
    # Removing leading zeros from first list
    while(head1 != None and head1.data == 0):
        head1 = head1.next
    # Removing leading zeros from second list
    while(head2 != None and head2.data == 0):
        head2 = head2.next
    # If both the lists contains only zeros
    if(head1 == None and head2 == None):
        temp = Node(0)
        return temp
    # If first list contains only zeros
    if(head1 == None):
        return head2
    # If second list contains only zeros
    if(head2 == None):
        return head1
    # Reverse both the linked lists
    head1 = reverse(head1)
    head2 = reverse(head2)
    ans = None
    traverse = None
    carry = 0
    # Add the linked lits
    while(head1 != None and head2 != None):
        temp = Node(0)
        sum = head1.data + head2.data + carry
        carry = sum // 10
        sum = sum % 10
        temp.data = sum
        if(ans == None):
            ans = temp
            traverse = temp
        else:
            traverse.next = temp
            traverse = traverse.next
        head1 = head1.next
        head2 = head2.next
    # Add the remaining linked list and the carry
    if(head1 != None):
        while(head1 != None):
            temp = Node(0)
            sum = head1.data + carry
            carry = sum // 10
            sum = sum % 10
            temp.data = sum
            traverse.next = temp
            traverse = traverse.next
            head1 = head1.next
    if(head2 != None):
        while(head2 != None):
            temp = Node(0)
            sum = head2.data + carry
            carry = sum // 10
            sum = sum % 10
            temp.data = sum
            traverse.next = temp
            traverse = traverse.next
            head2 = head2.next
    if(carry != 0):
        temp = Node(0)
        temp.data = carry
        traverse.next = temp
    ans = reverse(ans)
    return ans
