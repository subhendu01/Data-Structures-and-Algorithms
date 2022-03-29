# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None
    def addTwoNumbers(self, l1, l2, carry=0):
        if not l1 and not l2 and not carry: return None
        csum = carry
        if l1:
            csum += l1.val
            l1 = l1.next
        if l2:
            csum += l2.val
            l2 = l2.next
        head = ListNode(csum % 10, self.addTwoNumbers(l1, l2, csum > 9))
        return head

    # insert at end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = ListNode(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = ListNode(data, None)
    # insert list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
l1 = [2,4,3]
l2 = [5,6,4]
obj = Solution()

print(obj.addTwoNumbers(obj.insert_values(l1), obj.insert_values(l2)))