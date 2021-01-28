# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        while head is not None:
            temp_next = head.next
            head.next = prev
            prev = head
            head = temp_next
        return prev