# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Follow up: Could you do this in one pass?

 

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:

# Input: head = [1], n = 1
# Output: []

# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

class Solution:
    def removeNthFromEnd(self, head, n):
        length = 1
        temp = head
        while temp.next is not None:
            temp = temp.next
            length +=1
        if length == 1:
            return None
        if length == n:
            return head.next
        temp = head
        for x in range(1, length - n):
            temp = temp.next
        temp.next = temp.next.next
        return head