# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        res_head = ListNode()
        curr = res_head
        carry = 0
        p, q = l1, l2
        
        while p is not None or q is not None:
            x, y = 0, 0
            if p is None:
                x = 0
            else:
                x = p.val
                
            if q is None:
                y = 0
            else:
                y = q.val
            print(x, y)
            sum = x + y + carry
            
            if sum >= 10:
                carry = 1
            else:
                carry = 0
                
            curr.next = ListNode(sum % 10)
            curr = curr.next
            
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        
        if carry != 0:
            curr.next = ListNode(carry)
        
        return res_head.next