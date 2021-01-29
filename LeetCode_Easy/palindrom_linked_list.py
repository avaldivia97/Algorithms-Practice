# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head):
        traveler = head
        stack = []
        while traveler is not None:
            stack.append(traveler.val)
            traveler = traveler.next
        while head is not None:
            x = stack.pop()
            if x != head.val:
                return False
            head = head.next
        return True